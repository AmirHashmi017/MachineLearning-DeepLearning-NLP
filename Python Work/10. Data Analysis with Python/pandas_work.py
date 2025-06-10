import pandas as pd
# Creating Series. Series is a one dimensional array like structure.It is like a column of a table.DataFrame column
# is also series type
series1=pd.Series([1,2,3,4,5])
print(series1)
print(type(series1))
values=['amir','ashir','ali']
indexvalues=['a','b','c']
series2=pd.Series(values,index=indexvalues)
print(series2)
dictionary={'name':'Amir','Age':18,'City':'Lahore'}
series3=pd.Series(dictionary)
print(series3)
print(series2['a'])
print(series1[1:])

# DataFrame: DataFrame is a two Dimensional,size-mutable,heterogenious structure like a table with rows 
# and columns.Used to read CSVs And Excel files
dictionary={
    'name':['Amir','Ali','Ahmed'],
    'age':[18,21,19],
    'city':['Lahore','Toba Tek Singh','Lahore']
}
df=pd.DataFrame(dictionary)
# print(df)
dictionary=[
    {'name':'Amir','age':18,'city':'Lahore'},
    {'name':'Ali','age':21,'city':'Toba Tek Signh'},
    {'name':'Ahmad','age':19,'city':'Islamabad'}
]
df=pd.DataFrame(dictionary)
print(df)
# Acessing Element from DataFrame
print(df['name'])
# Access Based on labels means string indexes using loc
print(df.loc[1,'age':'city'])
# Access based on integer indexes
print(df.iloc[1:,1:])
# Access a specific element using label
print(df.at[0,'city'])
# Access a specific element using index
print(df.iat[0,2])
# Adding 1 to the age of all records
df['age']=df['age']+1
print(df)

# Adding a column
df['salary']=[500000,600000,700000]
print(df)
# Dropping a column inplace otherwise not delete
df.drop('salary',axis=1,inplace=True)
print(df)
# Inserting a new row
df.loc[3]=['Ashir',28,'Karachi']
# Dropping a row
df.drop(1,inplace=True)
print(df)
# Get statistical Info of Dataframe
print(df.describe())

# Reading a CSV File to DataFrame
csvdf=pd.read_csv("D:\\Github Repos\\AI-ML-Work\Python Work\\10. Data Analysis with Python\\sales_data.csv")
print(csvdf.head())
print(csvdf.tail())

print(csvdf.head(10))
print(csvdf.tail(10))