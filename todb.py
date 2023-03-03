import pandas as pd
import numpy as np
import sqlite3 as sl
import datetime
import socket

def read_file_to_db(text_file,db_file,date):
    #1000 iteration SSID selectionné arbitrairement, test à réaliser pour déterminer la valeur optimale
    con=sl.connect(db_file)
    Data=pd.read_table(text_file,header=None,sep=" ")
    X_SSID=Data.iloc[:,-1] #SSID de la capture
    X_time=Data.iloc[:,0 ] #Temps de la capture
    X_Address_MAC=Data.iloc[:,1]
    df_SSID=pd.DataFrame({'SSID' : X_SSID,'Time':X_time})
    df_SSID.to_sql(date,con,if_exists='replace',index=False)
    #date=table

today_date=datetime.datetime.now().strftime('%d-%m-%Y')

filename=r'CapProjet\\'+today_date+'.txt' #Ca on change
db_name="test.db" #Ca on change
read_file_to_db(filename,db_name,today_date)

#df=read_db(db_name,date)
#print(df)

