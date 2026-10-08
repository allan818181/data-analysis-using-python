import pandas as pd
df = pd.read_csv("olympics.csv")    
def show_columns(df):
    print("Display each column:")
    for col in df.columns:
        print(col)
    print("\n")

show_columns(df)
