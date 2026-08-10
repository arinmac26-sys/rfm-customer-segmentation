USE customer_rfm_analytics;

CREATE TABLE customer_master (
    CustomerID INT PRIMARY KEY,
    JoinDate DATE
);

CREATE TABLE customer_transactions (
    TransactionID BIGINT PRIMARY KEY AUTO_INCREMENT,
    CustomerID INT NOT NULL,
    TransactionDate DATE NOT NULL,
    TransactionAmount DECIMAL(14,2) NOT NULL,
    CONSTRAINT fk_transaction_customer
        FOREIGN KEY (CustomerID) REFERENCES customer_master(CustomerID)
);
