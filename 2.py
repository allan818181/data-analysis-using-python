import pandas as pd

df = pd.read_csv("olympics.csv")   

def show_dtypes(df):
    print("Display dtypes in this Excel:")
    print(df.dtypes)
    print("\n")

# 👉 Hii ndiyo ilikuwa inakosekana
show_dtypes(df)
