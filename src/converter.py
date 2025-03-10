import mysql.connector
import pandas as pd
from sqlalchemy import create_engine


# connect to database
engine = create_engine('mysql+mysqlconnector://root:Wuschtel5!@localhost/expenditure')

# read csv file
finland = pd.read_csv('data/csv/finland.csv')
print(finland.dtypes)

# drop columns
finland = finland.loc[:, ~finland.columns.str.contains('^Unnamed')]
# save to csv
finland.to_csv('data/csv/finland.csv', index=False)
print(finland.head())

# add to database (following code is commendted to not add the same data multiple times)
#finland.to_sql('valueYear', con=engine, if_exists='append', index=False)

spain = pd.read_csv('data/csv/spain.csv')
spain = spain.round()

spain = spain.loc[:, ~spain.columns.str.contains('^Unnamed')]
print(spain.head())

# add to database (following code is commendted to not add the same data multiple times)
#spain.to_sql('valueYear', con=engine, if_exists='append', index=False)