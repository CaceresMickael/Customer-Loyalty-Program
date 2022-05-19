import pandas as pd

file_name = (r'C:\Users\MICACERE\Documents\Customer-Loyalty-Program\Data_explo\data.csv')
df = pd.read_csv(file_name, encoding='unicode_escape',  sep = ",")
pd.set_option('display.max_columns', None)


# Check if an order as been canceled
#df['order_canceled'] = df['InvoiceNo'].apply(lambda x:int('C' in x))
#df.loc[df['order_canceled'] == 1]
#df[df['InvoiceNo'].str.contains('C') == True]

#Drop all row with a quantity inferior to 0
df = df.drop(df[df['Quantity'] < 0].index)

# Number of orders per country (can be the same per shop):
df.groupby(['Country']).agg({'InvoiceNo' : 'nunique'}).sort_values(by = "InvoiceNo", ascending= False)

# Number of clients per country:
df.groupby(['Country']).agg({'CustomerID' : 'nunique'}).sort_values(by = "CustomerID", ascending= False)

# Top 5 of product the most buy
df.groupby(["Description"]).agg({'Quantity' : 'sum'}).sort_values(by = "Quantity", ascending= False).head(5)

# Transform InvoiceDate to a datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], format= '%m/%d/%Y %H:%M')

df["date"] = pd.to_datetime(df["InvoiceDate"].dt.date , format='%Y-%m-%d') # add column date
df["time"] = df["InvoiceDate"].dt.time  # add column hours

# Quantity ordered per month 
df2 = pd.DataFrame(df[['date', 'Quantity']])
df2.groupby(pd.Grouper(freq='MS', key='date')).sum()
