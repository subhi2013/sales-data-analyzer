import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("sales_data.csv")
df["revenue"] = df["quantity"] * df["price"]
print(df)
total_revenue = df["revenue"].sum()
print("total revenue:" , total_revenue)
total_quantity = df["quantity"].sum()
print("total quantity:" , total_quantity)
best_product = df.loc[df["quantity"].idxmax()]
print("best selling product:")
print(best_product)
highest_revenue = df.loc[df["revenue"].idxmax()]
print("highest revenue product:")
print(highest_revenue)
plt.figure(figsize=(8,5))
plt.bar(df["product"],df["revenue"])
plt.title("revenue by product")
plt.xlabel("product")
plt.ylabel("revenue")
plt.grid()
plt.show()
plt.figure(figsize=(6,6))
plt.pie(df["revenue"],
        labels=df["product"],
        autopct="%1.1f%%",
        startangle=90
        )
plt.title("revenue distribution")
plt.show()
df.to_csv("sales_report.csv", index=False)
print("sales report saved successfully")
print("\n==========SALES REPORT========")
print("total products:" , len(df))
print("total quantity sold:", df["quantity"].sum())
print("total revenue:",
      df["revenue"].sum())
print("\nbest selling product:")
print(df.loc[df["quantity"].idxmax(),["product","quantity"]])
print("\nhighest revenue product:")
print(df.loc[df["revenue"].idxmax(), ["product", "revenue"]])