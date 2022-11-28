import pandas as pd

df = pd.read_csv("crust.csv", usecols = ['n','e','p'])
df.to_csv("crust.csv", sep=',', index=False)