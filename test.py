import pandas as pd
import numpy as np
import sqlite3 as sl
limit_max=1000 
#1000 iteration SSID selectionné arbitrairement, test à réaliser pour déterminer la valeur optimale
Data=pd.read_table(r"CapProjet\test.txt",header=None,sep=" ").to_numpy()  #Change le chemin d'accès du fichier
date="2020-05-01" #Date de la capture de données
con=sl.connect(r"CapProjet\test.db") #Change le chemin d'accès de la base de données
#date de la capture de données, normalement on modifie le .sh pour récupérer la date du jour
#pour avoir une suivie sur plusieurs jours, on peut créer une table par jour

X=Data[:,-1]
SSID=np.unique(X)
df_SSID=pd.DataFrame({'SSID' : [],'Number_SSID':[],'Risk':[]})
for x in SSID:
    Number_SSID=(np.count_nonzero(X==x))
    if x in df_SSID.SSID: #On vérifie si le SSID est déjà présent dans la table et on met à jour les valeurs
        #amélioration possible .update()
        df_SSID.loc[df_SSID.SSID==x,'Number_SSID']=Number_SSID
        df_SSID.loc[df_SSID.SSID==x,'Risk']=Number_SSID/limit_max
    else: #On ajoute le SSID à la table
        d2=pd.DataFrame({'SSID':x,'Number_SSID':Number_SSID,'Risk':Number_SSID/limit_max},index=[0])
        df_SSID.append(d2,ignore_index=True) ##Apppend deprecated, utiliser concat jsp comment

df_SSID.to_sql(date,con,if_exists='replace',index=False)
