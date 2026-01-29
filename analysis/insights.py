
import pandas as pd

def generate_insights(df):
    top_products = df.groupby('product_name')['total_sales'].sum().sort_values(ascending=False).head(5)
    revenue_by_region = df.groupby('region')['total_sales'].sum()
    return top_products, revenue_by_region
