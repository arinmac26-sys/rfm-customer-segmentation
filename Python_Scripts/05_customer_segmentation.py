import pandas as pd

rfm = pd.read_csv("../01_Data/cleaned/customer_rfm_scored.csv")

def segment(row):
    r, f, m = row["R_Score"], row["F_Score"], row["M_Score"]
    if r >= 4 and f >= 4 and m >= 4:
        return "Champions"
    if r >= 4 and f >= 3:
        return "Loyal Customers"
    if r >= 4 and m >= 3:
        return "Potential Loyalists"
    if r <= 2 and f >= 4:
        return "At Risk"
    if r <= 2 and m >= 4:
        return "Cannot Lose Them"
    if r <= 2 and f <= 2 and m <= 2:
        return "Lost Customers"
    return "Needs Attention"

rfm["Segment"] = rfm.apply(segment, axis=1)
rfm.to_csv("../01_Data/cleaned/customer_rfm_final.csv", index=False)
