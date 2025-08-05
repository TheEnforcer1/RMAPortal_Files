import pandas as pd

df = pd.read_csv('/home/drosete/RMAMonthly/data/MonthsRMAsData/2504_April_RMAs.csv')

sorted_df = df.sort_values(by='RMA No.')
#returns values sorted by RMA No.

unique_statuses = df['Status'].unique()

status_dataframes = {}
status_count = {}

for status in unique_statuses:
        status_df = df[df['Status'] == status]
        status_dataframes[status] = status_df
        status_count[status] = len(status_dataframes[status].index)

# Creating new CSV file/dataframe

MR_Dataset= pd.DataFrame(columns=[
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
        'New_Return'])


# Iteraring per RMA Value Row
for rma in status_dataframes['Completed'].values:
    # Finding total qty of Units
    model_num = rma[4]
    qty = rma[6]

    if model_num in MR_Dataset['Model'].values:
        prev_qty = MR_Dataset.loc[MR_Dataset['Model']== model_num, 'Total Qty'].values[0]
        MR_Dataset.loc[MR_Dataset['Model']== model_num, 'Total Qty'] = rma[6] + prev_qty
    else:
        MR_Dataset = MR_Dataset._append({'Model': rma[4], 'Total Qty':rma[6]}, ignore_index=True)



    ## Determining Unit Evaluation
    ## rma[12] is the Findings Column    
    ## rma[14] is the Resolution Column

    finding  = rma[12]
    resolution = rma[14]

    if finding  == 'Defective':
        if resolution == 'Replace(01)':
            prev_qty = MR_Dataset.loc[MR_Dataset['Model']== model_num, 'Total Qty'].values[0]
            MR_Dataset.loc[MR_Dataset['Model'] == rma[4], 'Defective_Replace(01)'] = qty + prev_qty
'''
    elif rma[12] == 'Working':

    if rma[12] == 'New(s)':
    
    else:
'''

print(MR_Dataset[['Model', 'Total Qty','Defective_Replace(01)']])
#print(status_dataframes['Completed'].values)

#for rma in status_dataframes['Completed'].values:






#print(MR_Dataset)



