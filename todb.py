import pandas as pd
import numpy as np
import sqlite3 as sl
import datetime

def read_file_to_db(text_file,db_file,date):
    con=sl.connect(db_file)
    Data=pd.read_table(text_file,header=None,sep=" ")
    X_SSID=Data.iloc[:,-1] #SSID de la capture
    X_time=Data.iloc[:,0 ] #Temps de la capture
    X_Address_MAC=Data.iloc[:,2] #Adresse Mac
    df_SSID=pd.DataFrame({'SSID' : X_SSID,'Time':X_time,'MAC':X_Address_MAC})
    df_traitements=df_SSID.groupby(['SSID','MAC','Time']).count().reset_index()
    df_traitements=df_traitements.sort_values(by=['Time'],ascending=True)
    df_traitements.to_sql(date,con,if_exists='replace',index=False)
    #date=table

today_date=datetime.datetime.now().strftime('%d-%m-%Y')

filename=today_date+'.txt'
db_name="SSID.db" 
read_file_to_db(filename,db_name,today_date)

#df=read_db(db_name,date)
#print(df)

