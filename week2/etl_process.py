
import pandas as pd

df = pd.read_csv("clean_ecommerce_sales.csv")
df['order_date'] = pd.to_datetime(df['order_date'])
df['unit_price'] = df['unit_price'].fillna(df['unit_price'].median())
df['total_sales'] = df['quantity'] * df['unit_price']
df.to_csv("clean_ecommerce_sales.csv", index=False)
print("ETL completed successfully")
