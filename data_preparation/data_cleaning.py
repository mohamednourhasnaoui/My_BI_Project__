
import pandas as pd

def clean_data():
    df = pd.read_csv("clean_ecommerce_sales.csv")
    df.fillna(0, inplace=True)
    df['total_sales'] = df['quantity'] * df['unit_price']
    df.to_csv("cleaned_sales.csv", index=False)

if __name__ == "__main__":
    clean_data()
