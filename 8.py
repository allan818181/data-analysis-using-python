import pandas as pd
df = pd.read_csv("olympics.csv")    

# def show_selected(df):
#     print("Q7. Columns: Edition, Medal, Gender, Sport")
#     print(df[["Edition", "Medal", "Gender", "Sport"]])
#     print("\n")

# show_selected(df)
def show_selected(df):
    print("Columns: Edition, Medal, Gender, Sport")

    needed = ["Edition", "Medal", "Gender", "Sport"]

    missing = [col for col in needed if col not in df.columns]

    if missing:
        print("❌ Missing columns:", missing)
        print("Available columns are:", list(df.columns))
    else:
        print(df[needed])
    print("\n")
