import pandas as pd
from pathlib import Path


data_column_headers = Path("Data/s_m_d_nagłówek.csv")
data_path = Path("Data/s_m_d_2024.csv")
ENCODING = "cp1250"


column_headers = []

#Reads column names from s_m_d_nagłówek.csv
with open(data_column_headers,mode="r",encoding=ENCODING) as f:
    text = f.read()
    #Replacing newline char
    text = text.replace("\n","")
    column_headers = text.split(",")




df = pd.read_csv(data_path,sep=",",header=None,encoding=ENCODING,names=column_headers)

df.to_csv("test.csv",index=False)
print(df.head())