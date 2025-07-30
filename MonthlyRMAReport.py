import pandas as pd

df = pd.read_csv('ItemsRMA.csv')

sorted_df = df.sort_values(by='RMA No.')
#returns values sorted by RMA No.

unique_statuses = df['Status'].unique()
status_dataframes = {}

monthly_df = df[df['RMA No.'].astype(str).str.startswith('2504')].sort_values(by='RMA No.')


monthly_status_dataframes = {
            status: monthly_df[monthly_df['Status'] == status].sort_values(by='RMA No.')
                for status in unique_statuses
}
#print(monthly_df)
#print(unique_statuses)

print(monthly_status_dataframes['Completed'])

