import pandas as pd
df = pd.read_csv("olympics.csv")    
def show_first_last_5(df):
    print("First 5 rows:")
    print(df.head())
    print("\nLast 5 rows:")
    print(df.tail())
    print("\n")

show_first_last_5(df)
