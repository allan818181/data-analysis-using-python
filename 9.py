import pandas as pd
df = pd.read_csv("olympics.csv")    

def describe_quant(df):
    print("Quantitative Summary:")
    print(df.describe())
    print("\n")

describe_quant(df)
