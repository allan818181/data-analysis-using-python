import pandas as pd
df = pd.read_csv("olympics.csv")    

def show_nulls(df):
    print("Null values per column:")
    print(df.isnull().sum())
    print("\n")

show_nulls(df)
