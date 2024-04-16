import pandas as pd
import datetime as dt
import research_lines_descriptors as rld

#print(rld.res_lines_list)

#################################################
# Reading the dataset with Pandas read_* method #
#################################################

csvfile = pd.read_csv('job_history.csv', delimiter=';', parse_dates=["Completed"])

# Rename the column
csvfile = csvfile.rename(columns={"Completed": "Date", "Model Material 1 Usage": "ABS", "Support Material 1 Usage": "QSR"})
#csvfile = 
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

grand_total = 0
for index, row in filtered_pddf.iterrows():
    for res_line in rld.res_lines_list:
        if row['Owner'] in res_line['owners']:
            print("porcodio")


    grand_total = grand_total+row['ABS']+row['QSR']




# print(filtered_pddf)
print(grand_total)


