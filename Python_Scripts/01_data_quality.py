import pandas as pd

master = pd.read_csv("../01_Data/raw/Customer_Master_Data.csv")
txn = pd.read_csv("../01_Data/raw/Customer_Transactions.csv")

print("Customer master shape:", master.shape)
print("Transactions shape:", txn.shape)
print("\nMaster missing values:\n", master.isna().sum())
print("\nTransaction missing values:\n", txn.isna().sum())
print("\nMaster duplicate rows:", master.duplicated().sum())
print("Transaction duplicate rows:", txn.duplicated().sum())
print("Unique master CustomerIDs:", master["CustomerID"].nunique())
print("Transaction CustomerIDs:", txn["CustomerID"].nunique())
