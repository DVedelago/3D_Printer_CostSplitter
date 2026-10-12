
# Rev 1.0 #

##################
# Import Modules #
##################

import pandas as pd
import datetime as dt
import glob
import os
from pathlib import Path
import research_lines_descriptors as rld
import sys

local_folder = Path("./")

if not os.path.exists("./merged"):
    os.makedirs("./merged")

merged_csv_filename = 'merged/printers_histories.csv'

joined_files = os.path.join(local_folder, '*.csv')
joined_list = glob.glob(joined_files)

# pd.read_csv alias to be used in map function
def read_csv_alias(f):
    return pd.read_csv(f, sep=";")

# merged dataframe
merged_dataframe = pd.concat(map(read_csv_alias, joined_list), ignore_index=True)

# merged csv
merged_dataframe.to_csv(merged_csv_filename, index=False, sep=";")



#################################################
# Reading the dataset with Pandas read_* method #
#################################################

csvfile = pd.read_csv(merged_csv_filename, sep=';', parse_dates=["Completed"])

# Rename the column
csvfile = csvfile.rename(columns={"Completed":                  "Date",
                                   "Model Material 1 Usage":    "ABS", 
                                   "Support Material 1 Usage":  "QSR"})

########################################################
# Creating DataFrame selecting only the columns needed #
########################################################

pddf = pd.DataFrame(
                    data=csvfile, 
                    columns=["Owner", "ABS", "QSR", "Date"],
                    )

##########################################
# Filtering by input[date] the DataFrame #
##########################################

date_from =  input("Enter Date in format YYYY-MM-DD: ")
date_from_datetype = pd.to_datetime((date_from))
print(date_from_datetype)


filtered_pddf = pddf.loc[(pddf['Date'] >= date_from_datetype) & (pddf['Date'] < pd.to_datetime("today"))]

######################################################
# Summing up the grand total of material consumption #
######################################################

# percentage on grand total;
def is_what_percent_of(num_a, num_b):                                                       
    try:
        return (num_a / num_b) * 100
    except ZeroDivisionError:
        return 0

######################################################
# Variables to store output                          #
######################################################

grand_total = 0

# list of unknown_users
unknown_users = []

# merge all users in a single list to compare against the printers histories CSV
big_list_of_owners = [] 

# creation of big_list_of_owners
for r in rld.res_lines_list:
    for u in r['owners']:
        big_list_of_owners.append(u)

# creation of unknown_users list
for i, userrow in filtered_pddf.iterrows():
    if userrow['Owner'] not in big_list_of_owners:
        if userrow['Owner'] not in unknown_users:
            unknown_users.append(userrow['Owner'])

if unknown_users:    
    print("**********")
    print("UNKNOWN USERS: ")
    print(unknown_users)
    print("**********")

else: print("All users match!")

print()

######################################################
# Main routine                                       #
######################################################

for index, row in filtered_pddf.iterrows():                                                 # cycle through the dataframe row by row;
    for res_line in rld.res_lines_list:                                                     # cycle through the research lines and their users;
        if row['Owner'] in res_line['owners']:                                              # check if the Owner match a research line;
            res_line['total_cm3'] = res_line["total_cm3"]+row['ABS']+row['QSR']             # sum the materials to the research line's accumulator;
        
        

        
    grand_total = grand_total+row['ABS']+row['QSR']


# TODO: check if prints are started in the weekend

###################
# Printing values #
###################

if not os.path.exists("./output"):
    os.makedirs("./output")

original_stdout = sys.stdout
filename = 'output/Cost_Split_Output-' + dt.datetime.now().strftime("%F_%H-%M") + '.txt'
with open(filename, 'x') as f:
    sys.stdout = f

    print()
    print('***************')
    print("Grand Total in cm^3 : ", "{:.3f}".format(grand_total))
    print('***************')
    print()

    for res_line2 in rld.res_lines_list:
        
        print('***************')
        
        print(res_line2['res_line_name'], ':', "{:.3f}".format(res_line2['total_cm3']))
        print("{0:.2f}%".format(is_what_percent_of(res_line2['total_cm3'], grand_total)), 'of Grand Total')
        
    print('***************')
f.close()
sys.stdout = sys.__stdout__

print("[**************************************]")
print("[ You can find the results in ./output ]")
print("[**************************************]")