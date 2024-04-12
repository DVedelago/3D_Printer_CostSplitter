import pandas as pd
import datetime as dt


#################################################
# Reading the dataset with Pandas read_* method #
#################################################

csvfile = pd.read_csv('job_history.csv', delimiter=';', parse_dates=["Completed"])

# Rename the column
csvfile = csvfile.rename(columns={"Completed": "Date"})

########################################################
# Creating DataFrame selecting only the columns needed #
########################################################

pddf = pd.DataFrame(
                    data=csvfile, 
                    columns=["Owner", "Model Material 1 Usage", "Support Material 1 Usage", "Date"],
                    )

##########################################
# Filtering by input[date] the DataFrame #
##########################################

#date_from = input("Enter Date in format YYYY-MM-DD: ")
dt.datetime(date_from)
#date_filtered_pddf = 

filtered_pddf = pddf.loc[(pddf['Date'] >= '2024-01-01') & (pddf['Date'] < pd.to_datetime("today").date())]
######################################################
# Summing up the grand total of material consumption #
######################################################




print(filtered_pddf)
print(date_from)


