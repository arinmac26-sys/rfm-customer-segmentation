import pandas as pd

master = pd.read_csv("../01_Data/raw/Customer_Master_Data.csv")
txn = pd.read_csv("../01_Data/raw/Customer_Transactions.csv")

for df in (master, txn):
    for c in df.select_dtypes(include="object").columns:
        df[c] = df[c].astype("string").str.strip()

master["JoinDate"] = pd.to_datetime(master["JoinDate"], errors="coerce")
txn["TransactionDate"] = pd.to_datetime(txn["TransactionDate"], errors="coerce")
txn["TransactionAmount"] = pd.to_numeric(txn["TransactionAmount"], errors="coerce")

master = master.drop_duplicates()
txn = txn.drop_duplicates()

valid_ids = set(master["CustomerID"].dropna().unique())
txn = txn[txn["CustomerID"].isin(valid_ids)]

master.to_csv("../01_Data/cleaned/customer_master_cleaned.csv", index=False)
txn.to_csv("../01_Data/cleaned/customer_transactions_cleaned.csv", index=False)
