
import pandas as pd

def run_etl():
    df = pd.read_csv("clean_ecommerce_sales.csv")
    df.dropna(inplace=True)
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['total_sales'] = df['quantity'] * df['unit_price']
    df.to_csv("processed_sales.csv", index=False)

if __name__ == "__main__":
    run_etl()
