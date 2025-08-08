import pandas as pd

df = pd.read_csv('/home/drosete/RMAMonthly/data/MonthsRMAsData/2501_January_RMAs.csv')

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
        'Vendor',
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

MiscRMAs = []

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


    MR_Dataset.fillna(0, inplace=True)
    MR_Dataset = MR_Dataset.infer_objects()
    MR_Dataset = MR_Dataset.astype({col: 'int' for col in MR_Dataset.select_dtypes(include='number').columns})

    ## Determining Unit Evaluation
    ## rma[12] is the Findings Column    
    ## rma[14] is the Resolution Column

    finding  = rma[12]
    resolution = rma[14]

    if finding  == 'Defective' or finding == 'Customer will not return':
        if resolution == 'Replace(01)':    
            prev_qty = MR_Dataset.loc[MR_Dataset['Model']== model_num, 'Defective_Replace(01)'].values[0]
            MR_Dataset.loc[MR_Dataset['Model'] == model_num, 'Defective_Replace(01)'] = qty + prev_qty
        elif resolution == 'Replace(90)':
            prev_qty = MR_Dataset.loc[MR_Dataset['Model']== model_num, 'Defective_Replace(90)'].values[0]
            MR_Dataset.loc[MR_Dataset['Model'] == model_num, 'Defective_Replace(90)'] = qty + prev_qty
        
        elif resolution == 'Issue Credit':
            prev_qty = MR_Dataset.loc[MR_Dataset['Model']== model_num, 'Defective_Credit'].values[0]
            MR_Dataset.loc[MR_Dataset['Model'] == model_num, 'Defective_Credit'] = qty + prev_qty
        elif resolution == 'Repair':
            prev_qty = MR_Dataset.loc[MR_Dataset['Model']== model_num, 'Defective_Repair'].values[0]
            MR_Dataset.loc[MR_Dataset['Model'] == model_num, 'Defective_Repair'] = qty + prev_qty
        elif resolution == 'Return' or resolution == 'Discard':
            prev_qty = MR_Dataset.loc[MR_Dataset['Model']== model_num, 'Defective_Return'].values[0]
            MR_Dataset.loc[MR_Dataset['Model'] == model_num, 'Defective_Return'] = qty + prev_qty
        else:
            MiscRMAs.append(rma[0])

    elif finding == 'Tested to be working':
        if resolution == 'Replace(01)':    
            prev_qty = MR_Dataset.loc[MR_Dataset['Model']== model_num, 'Working_Replace(01)'].values[0]
            MR_Dataset.loc[MR_Dataset['Model'] == model_num, 'Working_Replace(01)'] = qty + prev_qty

        elif resolution == 'Replace(90)':    
            prev_qty = MR_Dataset.loc[MR_Dataset['Model']== model_num, 'Working_Replace(90)'].values[0]
            MR_Dataset.loc[MR_Dataset['Model'] == model_num, 'Working_Replace(90)'] = qty + prev_qty

        elif resolution == 'Return':    
            prev_qty = MR_Dataset.loc[MR_Dataset['Model']== model_num, 'Working_Return'].values[0]
            MR_Dataset.loc[MR_Dataset['Model'] == model_num, 'Working_Return'] = qty + prev_qty
  
        elif resolution == 'Issue Credit':    
            prev_qty = MR_Dataset.loc[MR_Dataset['Model']== model_num, 'Working_Credit'].values[0]
            MR_Dataset.loc[MR_Dataset['Model'] == model_num, 'Working_Credit'] = qty + prev_qty
        else:
            MiscRMAs.append(rma[0])

    elif finding == 'New unit(s)':
        if resolution == 'Issue Credit':    
            prev_qty = MR_Dataset.loc[MR_Dataset['Model']== model_num, 'New_Credit'].values[0]
            MR_Dataset.loc[MR_Dataset['Model'] == model_num, 'New_Credit'] = qty + prev_qty
        elif resolution == 'Return':    
            prev_qty = MR_Dataset.loc[MR_Dataset['Model']== model_num, 'New_Return'].values[0]
            MR_Dataset.loc[MR_Dataset['Model'] == model_num, 'New_Return'] = qty + prev_qty
        else:
            MiscRMAs.append(rma[0])
    else:
        MiscRMAs.append(rma[0])
        
        
#print(MR_Dataset[['Model', 'Total Qty','Defective_Replace(01)']])
#prev_qty = MR_Dataset.loc[MR_Dataset['Model'] == 'SK-B141-PQ', 'Total Qty'].values[0]
#print(prev_qty)

#print(status_dataframes['Completed'].values)

#for rma in status_dataframes['Completed'].values:





MR_Dataset.to_csv('output.csv', index=False)


print(MR_Dataset)
print(MiscRMAs)



