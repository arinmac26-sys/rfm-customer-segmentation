import pandas as pd

txn = pd.read_csv("../01_Data/cleaned/customer_transactions_cleaned.csv")
txn["TransactionDate"] = pd.to_datetime(txn["TransactionDate"], errors="coerce")
txn["TransactionAmount"] = pd.to_numeric(txn["TransactionAmount"], errors="coerce")

reference_date = txn["TransactionDate"].max()

rfm = txn.groupby("CustomerID").agg(
    LastPurchaseDate=("TransactionDate", "max"),
    Frequency=("TransactionDate", "count"),
    Monetary=("TransactionAmount", "sum")
).reset_index()

rfm["Recency"] = (reference_date - rfm["LastPurchaseDate"]).dt.days
rfm = rfm[["CustomerID", "Recency", "Frequency", "Monetary", "LastPurchaseDate"]]

rfm.to_csv("../01_Data/cleaned/customer_rfm_base.csv", index=False)
print(rfm.head())
