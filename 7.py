import pandas as pd
df = pd.read_csv("olympics.csv")    

def drop_missing(df):
    print("After dropping all missing rows:")
    clean = df.dropna()
    print(clean)
    print("\n")
    return clean

df_clean = drop_missing(df)
