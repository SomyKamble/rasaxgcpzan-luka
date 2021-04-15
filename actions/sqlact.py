#import pyodbc
import sqlalchemy
import pymssql
from sqlalchemy import create_engine
import pandas as pd

# Name: pyodbc
# Version: 4.0.30

# Name: SQLAlchemy
# Version: 1.3.23

def activity_count(act):

    # server = "DESKTOP-K23NHA9"
    #
    # database = "zan&luka"

    engine = create_engine('mssql+pymssql://sqlserver:$So9423637191@34.71.157.91/zan&luka')

    # engine = create_engine('mssql+pyodbc://' + server + '/' + database + '?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server')


    connection = engine.connect()
    flag=0
    print(engine.table_names())
    for i in engine.table_names():
        if act in i:
            print(i)
            flag=1
            break


    if flag==1:
        query = "Select * from dbo.{}".format(i)
        sa = pd.read_sql(query, connection)
        #print(sa)
        return sa
    else:
        return "not found"


