# Data Cleaning & Quality Process

1. Load customer master and transaction data.
2. Inspect shape, columns, data types and sample records.
3. Trim whitespace from string columns.
4. Convert `JoinDate` and `TransactionDate` to datetime.
5. Convert `TransactionAmount` to numeric.
6. Remove exact duplicate records.
7. Validate CustomerID uniqueness in the master dataset.
8. Validate transaction CustomerIDs against the master dataset.
9. Retain valid transaction records for downstream RFM analysis.
10. Export cleaned datasets to `01_Data/cleaned/`.

The cleaning script is intentionally separated from the notebook so the portfolio project is reproducible outside Jupyter.
