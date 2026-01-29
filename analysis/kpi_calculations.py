
import pandas as pd

def calculate_kpis(df):
    total_revenue = df['total_sales'].sum()
    total_orders = df['order_id'].nunique()
    aov = total_revenue / total_orders
    return total_revenue, total_orders, aov
