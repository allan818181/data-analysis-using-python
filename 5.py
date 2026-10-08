import pandas as pd
df = pd.read_csv("olympics.csv")    

def show_last_25_10(df):
    print("Last 25 rows:")
    print(df.tail(25))
    print("\nLast 10 rows:")
    print(df.tail(10))
    print("\n")

show_last_25_10(df)
