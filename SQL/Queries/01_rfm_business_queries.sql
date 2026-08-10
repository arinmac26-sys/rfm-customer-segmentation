USE customer_rfm_analytics;

-- Segment customer count
SELECT Segment, COUNT(*) AS Customers
FROM customer_rfm
GROUP BY Segment
ORDER BY Customers DESC;

-- Revenue by segment
SELECT Segment,
       COUNT(*) AS Customers,
       SUM(Monetary) AS Revenue
FROM customer_rfm
GROUP BY Segment
ORDER BY Revenue DESC;

-- Highest-value customers
SELECT *
FROM customer_rfm
ORDER BY Monetary DESC
LIMIT 20;

-- At-risk customers
SELECT *
FROM customer_rfm
WHERE Segment IN ('At Risk', 'Cannot Lose Them')
ORDER BY Monetary DESC;

-- RFM score distribution
SELECT RFM_Score, COUNT(*) AS Customers
FROM customer_rfm
GROUP BY RFM_Score
ORDER BY RFM_Score;
