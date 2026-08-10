-- Portfolio load template.
-- Bulk-load commands vary by MySQL client/environment.
-- Example:

LOAD DATA LOCAL INFILE 'Customer_Master_Data.csv'
INTO TABLE customer_master
FIELDS TERMINATED BY ','
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE 'Customer_Transactions.csv'
INTO TABLE customer_transactions
FIELDS TERMINATED BY ','
IGNORE 1 ROWS
(CustomerID, TransactionDate, TransactionAmount);
