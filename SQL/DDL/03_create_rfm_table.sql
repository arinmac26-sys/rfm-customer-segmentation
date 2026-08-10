USE customer_rfm_analytics;

CREATE TABLE customer_rfm (
    CustomerID INT PRIMARY KEY,
    Recency INT,
    Frequency INT,
    Monetary DECIMAL(14,2),
    R_Score TINYINT,
    F_Score TINYINT,
    M_Score TINYINT,
    RFM_Score VARCHAR(3),
    Segment VARCHAR(50),
    LastPurchaseDate DATE,
    CONSTRAINT fk_rfm_customer
        FOREIGN KEY (CustomerID) REFERENCES customer_master(CustomerID)
);
