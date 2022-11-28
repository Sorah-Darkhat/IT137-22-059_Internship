import pandas as pd

df = pd.read_csv("DDB_l.txt", sep="  ")
print(df)
df.to_csv("DBBL_C.csv")