import pandas as pd
import csv
from pathlib import Path
from config import COLUMNS_TO_KEEP_S_M_D


data_column_headers = Path("Data/raw/readable_column_headers.csv")
data_path = Path("Data/raw/s_m_d_2024.csv")
ENCODING = "cp1250"

# Status "8" brak pomiaru
# Status "9" brak zjawiska
# Dla agregacji typu "Liczba dni z" status "9" oznacza brak pomiaru zjawisk na stacji.

column_headers = []

#Reads column names from s_m_d_nagłówek.csv
with open(data_column_headers,newline="",encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        column_headers.append(row["long_name_en"])



df = pd.read_csv(data_path,sep=",",header=None,encoding=ENCODING,names=column_headers)
df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")



df["station_name"] = (df["station_name"]
                        .str.lower()
                        .str.strip()
                        .str.replace(r"[\s-]+", "_", regex=True)
)

df = df[COLUMNS_TO_KEEP_S_M_D]
df.to_csv("test.csv",index=False)
#print(df.head())
#df.info()
#df.describe().to_csv("stats.csv",index=False)
#print(df.isna().sum())

