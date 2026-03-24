import pandas as pd
df=pd.read_csv('olympics.csv')
if __name__ == "__main__":
    rows, cols = df.shape
    print(f"Rows: {rows}")
    print(f"Columns: {cols}")



