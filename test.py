import pandas as pd
import numpy as np
import sqlite3 as sl

def read_file_to_db(text_file,db_file,date):
    limit_max=1000 
    #1000 iteration SSID selectionné arbitrairement, test à réaliser pour déterminer la valeur optimale
    Data=pd.read_table(text_file,header=None,sep=" ").to_numpy()
    con=sl.connect(db_file)
    X=Data[:,-1] #
    SSID=np.unique(X)
    df_SSID=pd.DataFrame({'SSID' : [],'Number_SSID':[],'Risk':[]})
    for x in SSID:
        Number_SSID=(np.count_nonzero(X==x))
        d1=df_SSID
        d2=pd.DataFrame({'SSID':x,'Number_SSID':Number_SSID,'Risk':(Number_SSID/limit_max)*100},index=[0])
        #Risk, un pourchentage(0% à 100%)
        df_SSID=pd.concat([d1,d2])
    df_SSID.to_sql(date,con,if_exists='replace',index=False)
    #date de la capture de données, normalement on modifie le .sh pour récupérer la date du jour
    #pour avoir une suivie sur plusieurs jours, on peut créer une table par jour
    #date=table

def read_db(db_file,date):
    con=sl.connect(db_file)
    df = pd.read_sql_query("SELECT * from '"+date+"'", con)
    con.close()
    return df

filename="test.txt"
db_name="test.db"
date="2023-01-24"
read_file_to_db(filename,db_name,date)
df=read_db(db_name,date)
print(df)