import mysql.connector
import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('data/csv/finland.csv')
print(df.dtypes)

df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
print(df.head())

engine = create_engine('mysql+mysqlconnector://root:Wuschtel5!@localhost/expenditure')
df.to_sql('valueYear', con=engine, if_exists='append', index=False)