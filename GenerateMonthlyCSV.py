import pandas as pd

df = pd.read_csv('/home/drosete/RMAMonthly/data/ItemsRMA.csv')


df = df.drop(columns= [
            'RMA Date',
            'Account No.',
            'Requested On',
            'Sales Doc. No.',
            'PO # (For Advanced Replacements only)',
            'Transfer to Warehouse Remarks'])


months = {
                '2501': 'January',
                '2502': 'February',
                '2503': 'March',
                '2504': 'April',
                '2505': 'May',
                '2506': 'June',
                '2507': 'July',
                '2508': 'August',
                '2509': 'September',
                '2510': 'October',
                '2511': 'November',
                '2512': 'Decemeber'}


#monthly_df = df[df['RMA No.'].astype(str).str.startswith('2504')].sort_values(by='RMA No.')


#monthly_df.to_csv('AprilRMAs.csv', index=False  )


for i in months:
    monthly_df = df[df['RMA No.'].astype(str).str.startswith(i)].sort_values(by='RMA No.')
    filename = f"{i.replace(' ','_')}_{months[i].replace(' ','_')}_RMAs.csv"
    
    filepath = '/home/drosete/RMAMonthly/data/MonthsRMAsData/'+ filename

    monthly_df.to_csv(filepath, index=False)
    #monthly_df.to_csv('AprilRMAs.csv', index=False  )
    

    #print(monthly_df)
    





print("Done")
