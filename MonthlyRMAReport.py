import pandas as pd

df = pd.read_csv('/home/drosete/RMAMonthly/data/MonthsRMAsData/2504_April_RMAs.csv')

sorted_df = df.sort_values(by='RMA No.')
#returns values sorted by RMA No.

unique_statuses = df['Status'].unique()

#print(unique_statuses)

status_dataframes = {}
status_count = {}

for status in unique_statuses:
        status_df = df[df['Status'] == status]
        status_dataframes[status] = status_df
        status_count[status] = len(status_dataframes[status].index)


#example of calling a specific dataframe from status_dataframe dictionary
#print(status_dataframes['Completed'])

#prnts all columns
#print(status_dataframes['Completed'].columns)

print(status_count)

Monthly_Report_Columns = [
        'Model',
        'Total Qty',
        'Defective_Return',
        'Defective_Repair',
        'Defective_Replace(01)',
        'Defective_Replace(90)',
        'Defective_Credit',
        'Working_Return',
        'Working_Replace(01)',
        'Working_Replace(90)',
        'Working_Credit',
        'New_Credit',
        'New_Return']





'''
status_dataframes = {}

monthly_df = df[df['RMA No.'].astype(str).str.startswith('2504')].sort_values(by='RMA No.')


monthly_status_dataframes = {
            status: monthly_df[monthly_df['Status'] == status].sort_values(by='RMA No.')
                for status in unique_statuses
}
#print(monthly_df)

print(monthly_status_dataframes['Issued RMA'])
print("Issued RMA CSV file donwnloaded")

df_monthlyDict = pd.DataFrame(monthly_status_dataframes)
df_monthlyDict.to_csv("April_IssuedRMAs.csv")

#print(unique_statuses)



df = df.drop(columns= [
        'RMA Date',
        'Account No.',
        'Requested On',
        'Sales Doc. No.',
        'PO # (For Advanced Replacements only)',
        'Transfer to Warehouse Remarks'
        ])

monthly_df = df[df['RMA No.'].astype(str).str.startswith('2504')].sort_values(by='RMA No.')




for status in unique_statuses: 
    status_df = monthly_df[monthly_df['Status'] == status]
    filename = f"{status.replace(' ', '_')}_Arpil.csv"
    status_df.to_csv(filename, index=False)
    print(status_df)

print("done")

print(status_df)
'''


