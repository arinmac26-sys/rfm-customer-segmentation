# Project Architecture

```text
                 ┌─────────────────────────┐
                 │ Customer Master CSV     │
                 └────────────┬────────────┘
                              │
                 ┌────────────▼────────────┐
                 │ Customer Transactions   │
                 └────────────┬────────────┘
                              │
                       Data Quality
                              │
                       Data Cleaning
                              │
                    Customer ID Validation
                              │
                        RFM Engine
                              │
              ┌───────────────┼───────────────┐
              │               │               │
           Recency         Frequency       Monetary
              │               │               │
              └───────────────┼───────────────┘
                              │
                        RFM Scoring
                              │
                         Segmentation
                              │
             ┌────────────────┼────────────────┐
             │                │                │
         Segment Count    Revenue Mix      Pareto
             │                │                │
             └────────────────┼────────────────┘
                              │
                     Business Actions
```
