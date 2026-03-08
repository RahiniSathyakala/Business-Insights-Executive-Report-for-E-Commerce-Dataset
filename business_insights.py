import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Online Retail.csv", encoding="ISO-8859-1")

# Convert date
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# Remove missing customers
df = df.dropna(subset=["CustomerID"])

# Create sales column
df["Sales"] = df["Quantity"] * df["UnitPrice"]

# -------------------------
# 1 Total Revenue
# -------------------------
total_revenue = df["Sales"].sum()
print("Total Revenue:", total_revenue)

# -------------------------
# 2 Top Selling Products
# -------------------------
top_products = df.groupby("Description")["Quantity"].sum().sort_values(ascending=False).head(10)

print("\nTop Products:")
print(top_products)

plt.figure(figsize=(8,5))
top_products.plot(kind="bar")
plt.title("Top Selling Products")
plt.ylabel("Quantity Sold")
plt.show()

# -------------------------
# 3 Sales by Country
# -------------------------
country_sales = df.groupby("Country")["Sales"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(8,5))
country_sales.plot(kind="bar")
plt.title("Top Countries by Revenue")
plt.ylabel("Sales")
plt.show()

# -------------------------
# 4 Monthly Revenue Trend
# -------------------------
df["Month"] = df["InvoiceDate"].dt.to_period("M")

monthly_sales = df.groupby("Month")["Sales"].sum()

monthly_sales.index = monthly_sales.index.to_timestamp()

plt.figure(figsize=(10,5))
plt.plot(monthly_sales)
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

print("\nBusiness Analysis Completed")