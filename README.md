# 🎯 RFM Customer Segmentation | Senior Data Analytics Portfolio

> **End-to-end customer analytics project using Python, SQL, RFM modeling, customer segmentation and business intelligence.**

![Python](https://img.shields.io/badge/Python-Analytics-3776AB?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-150458?logo=pandas&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-Analytics-orange)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Portfolio-181717?logo=github&logoColor=white)

## 📌 Project Overview

This project uses **RFM (Recency, Frequency, Monetary) analysis** to understand customer value and translate transaction history into actionable customer segments.

The project follows a production-style analytics workflow:

```text
Raw Data
   ↓
Data Quality Assessment
   ↓
Data Cleaning & Validation
   ↓
Customer / Transaction Integration
   ↓
RFM Calculation
   ↓
RFM Scoring
   ↓
Customer Segmentation
   ↓
Visualization & Pareto Analysis
   ↓
Business Recommendations
```

## 🎯 Business Objective

Answer key customer analytics questions:

- Which customers are most valuable?
- Which customers are loyal?
- Which customers are becoming inactive?
- Which high-value customers are at risk?
- Which customers need reactivation?
- How should marketing investment be prioritized?

## 🧰 Technology Stack

- **Python**
- **Pandas / NumPy**
- **Matplotlib / Seaborn**
- **SciPy**
- **Jupyter Notebook**
- **SQL / MySQL**
- **Git / GitHub**

## 📂 Repository Structure

```text
RFM_Customer_Segmentation/
│
├── 01_Data/
│   ├── raw/
│   └── cleaned/
│
├── 02_Notebooks/
│   └── Arindam_Das_Biswas_RFM_Customer_Segmentation.ipynb
│
├── 03_Python_Scripts/
│   ├── 01_data_quality.py
│   ├── 02_data_cleaning.py
│   ├── 03_rfm_calculation.py
│   ├── 04_rfm_scoring.py
│   └── 05_customer_segmentation.py
│
├── 04_SQL/
│   ├── DDL/
│   ├── DML/
│   └── Queries/
│
├── 05_Analysis/
│   ├── Data_Quality/
│   ├── RFM/
│   ├── Segmentation/
│   └── Pareto/
│
├── 06_Visualizations/
│
├── 07_Dashboard/
│
├── 08_Diagrams/
│   ├── ERD.png
│   ├── ERD.md
│   └── PROJECT_ARCHITECTURE.png
│
├── 09_Documentation/
├── 10_Reports/
└── 11_Project_Assets/
```

## 🧹 Data Cleaning

The project separates data preparation from analytical logic.

Key steps:

1. Load customer master and transaction datasets.
2. Inspect structure and data quality.
3. Standardize text fields.
4. Convert date fields.
5. Validate numeric transaction amounts.
6. Remove duplicate rows.
7. Validate CustomerID relationships.
8. Produce cleaned datasets for RFM analysis.

See [`09_Documentation/DATA_CLEANING.md`](09_Documentation/DATA_CLEANING.md).

## 📊 RFM Methodology

### Recency

Measures how recently a customer purchased.

```text
Recency = Reference Date - Last Purchase Date
```

**Lower is better.**

### Frequency

Measures transaction frequency.

```text
Frequency = Number of Transactions
```

**Higher is better.**

### Monetary

Measures customer value.

```text
Monetary = Total Transaction Amount
```

**Higher is better.**

## 🏷️ Customer Segmentation

The portfolio model creates business-oriented segments:

| Segment | Strategic Action |
|---|---|
| 🏆 Champions | Retain, reward and create advocates |
| 💎 Loyal Customers | Cross-sell and upsell |
| 🌱 Potential Loyalists | Encourage repeat purchase |
| ⚠️ At Risk | Reactivation campaigns |
| 🚨 Cannot Lose Them | High-priority retention |
| 💤 Lost Customers | Cost-efficient win-back |
| 🔎 Needs Attention | Further customer analysis |

## 📈 Visualization Gallery

All charts extracted from the executed notebook are stored as `.png` files under:

`06_Visualizations/`

This makes the repository recruiter-friendly and allows charts to be viewed directly on GitHub.

## 🗄️ SQL Data Model

The repository includes a derived SQL analytical model:

```text
CUSTOMER_MASTER
       │
       ├──────────< CUSTOMER_TRANSACTIONS
       │
       └──────────  CUSTOMER_RFM
```

SQL is organized into:

- **DDL** — database and table definitions
- **DML** — data loading
- **Queries** — business analysis

> The SQL model is a portfolio analytical representation of the source files; it is not claimed to be the original production database schema.

## 💼 Business Impact

RFM segmentation can support:

- Customer retention
- CRM campaign targeting
- Reactivation programs
- Loyalty programs
- Cross-sell / upsell
- Marketing budget allocation
- Customer lifetime value initiatives

## 🔬 Senior Analyst Skills Demonstrated

### Data Engineering
- Data ingestion
- Data validation
- Data transformation
- Relational modeling

### Analytics
- RFM methodology
- Customer segmentation
- Aggregation
- Revenue analysis
- Pareto analysis

### Technical
- Python
- Pandas
- SQL
- Jupyter
- Git/GitHub

### Business
- Customer lifecycle analysis
- Retention strategy
- Marketing prioritization
- Actionable segmentation

## ▶️ How to Run

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd RFM_Customer_Segmentation

pip install -r 11_Project_Assets/requirements.txt

jupyter notebook 02_Notebooks/Arindam_Das_Biswas_RFM_Customer_Segmentation.ipynb
```

For the modular pipeline, run the scripts under `03_Python_Scripts/` in sequence.

## 👤 Author

**Arindam Das Biswas**

Senior Data Analytics Portfolio

**Core Skills:** Python • SQL • Data Analytics • Customer Analytics • RFM • Data Cleaning • Statistical Analysis • Business Intelligence • Data Visualization
