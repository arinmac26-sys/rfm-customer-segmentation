# Data Dictionary

## Customer_Master_Data

| Field | Business Meaning |
|---|---|
| CustomerID | Unique customer identifier |
| Customer attributes | Customer master/profile attributes |
| JoinDate | Customer onboarding/join date |

## Customer_Transactions

| Field | Business Meaning |
|---|---|
| CustomerID | Customer identifier linking to master |
| TransactionDate | Date of customer transaction |
| TransactionAmount | Monetary value of transaction |

## RFM Output

| Field | Meaning |
|---|---|
| Recency | Days since customer's most recent purchase |
| Frequency | Number of transactions |
| Monetary | Total transaction value |
| R_Score | Recency quintile score |
| F_Score | Frequency quintile score |
| M_Score | Monetary quintile score |
| RFM_Score | Combined three-digit RFM score |
| Segment | Business-facing customer segment |
