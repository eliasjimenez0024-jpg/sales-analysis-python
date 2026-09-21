import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/sales_data.csv")

df["sales"] = df["units"] * df["unit_price"]

total_sales = df["sales"].sum()
total_units = df["units"].sum()
average_order_value = df["sales"].mean()

sales_by_product = (
    df.groupby("product")["sales"].sum().sort_values(ascending=False)
)

sales_by_region = (
    df.groupby("region")["sales"].sum().sort_values(ascending=False)
)

sales_by_salesperson = (
    df.groupby("salesperson")["sales"].sum().sort_values(ascending=False)
)

sales_by_product_pct = (sales_by_product / total_sales) * 100
sales_by_region_pct = (sales_by_region / total_sales) * 100
sales_by_salesperson_pct = (sales_by_salesperson / total_sales) * 100


df["date"] = pd.to_datetime(df["date"])

df["month"] = df["date"].dt.to_period("M")

monthly_sales = (
    df.groupby("month")["sales"].sum()
)

sales_by_category = (
    df.groupby("category")["sales"].sum().sort_values(ascending=False)
)

sales_by_category_pct = (sales_by_category / total_sales) * 100

print(df.head())

print("Total sales: ", total_sales)
print("Total units: ", total_units)
print("Average Order Value: ", average_order_value)

print("\nSales by Product:")
print(sales_by_product)

print("\nSales by Region:")
print(sales_by_region)

print("\nSales by Salesperson:")
print(sales_by_salesperson)

print("\nSales by Product %:")
print(sales_by_product_pct.round(2))

print("\nSales by Region %:")
print(sales_by_region_pct.round(2))

print("\nSales by Salesperson %:")
print(sales_by_salesperson_pct.round(2))

print("\nSales by Month")
print(monthly_sales)

print("\nSales by Category")
print(sales_by_category)

print("\nSales by Category %:")
print(sales_by_category_pct.round(2))

monthly_sales.plot(kind="bar")

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.tight_layout()

plt.savefig("outputs/monthly_sales.png")

plt.show()