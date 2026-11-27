"""Phase 1 cleaning for DS-599 churn capstone.
Usage: python clean_data.py <raw_dir> <out_dir>
raw_dir must contain telco.csv (Kaggle blastchar), bank.csv (Kaggle shrutimechlearn), iran.csv (UCI 563).
Model-dependent steps (scaling, one-hot, resampling) are NOT applied here: they are fitted
inside a scikit-learn Pipeline on the training split only, to avoid leakage."""
import sys, pandas as pd, numpy as np
raw, out = sys.argv[1], sys.argv[2]
log = {}

# ---------- Telco ----------
t = pd.read_csv(f"{raw}/telco.csv")
blank = t.TotalCharges.str.strip() == ""
assert (t.loc[blank, "tenure"] == 0).all()          # all blanks are brand-new customers
t["TotalCharges"] = pd.to_numeric(t.TotalCharges, errors="coerce").fillna(0.0)
t = t.drop(columns="customerID")
for c in ["MultipleLines","OnlineSecurity","OnlineBackup","DeviceProtection","TechSupport","StreamingTV","StreamingMovies"]:
    t[c] = t[c].replace({"No internet service": "No", "No phone service": "No"})
for c in ["Partner","Dependents","PhoneService","PaperlessBilling","Churn","MultipleLines","OnlineSecurity",
          "OnlineBackup","DeviceProtection","TechSupport","StreamingTV","StreamingMovies"]:
    t[c] = t[c].map({"Yes": 1, "No": 0})
t["gender"] = t.gender.map({"Male": 1, "Female": 0}); t = t.rename(columns={"gender": "IsMale"})
log["telco"] = (t.shape, t.Churn.mean())
t.to_csv(f"{out}/telco_clean.csv", index=False)

# ---------- Bank ----------
b = pd.read_csv(f"{raw}/bank.csv")
b = b.drop(columns=["RowNumber", "CustomerId", "Surname"])
b["IsMale"] = (b.Gender == "Male").astype(int); b = b.drop(columns="Gender")
b["ZeroBalance"] = (b.Balance == 0).astype(int)
b["NumOfProducts"] = b.NumOfProducts.clip(upper=3)   # 3 and 4 merged into "3+" (4 = 60 rows, 100% churn)
b["LowSalaryFlag"] = (b.EstimatedSalary < 1000).astype(int)
b = b.rename(columns={"Exited": "Churn"})
log["bank"] = (b.shape, b.Churn.mean())
b.to_csv(f"{out}/bank_clean.csv", index=False)

# ---------- Iran ----------
i = pd.read_csv(f"{raw}/iran.csv")
i.columns = [" ".join(c.split()).replace(" ", "_") for c in i.columns]
n0 = len(i); i = i.drop_duplicates().reset_index(drop=True)
i = i.drop(columns="Age")                              # deterministic copy of Age_Group
i["Tariff_Plan"] = (i.Tariff_Plan == 2).astype(int)   # 1=pay-as-you-go, 2=contractual
i["Status"] = (i.Status == 1).astype(int)             # 1=active, 2=non-active -> 1/0
i["Inactive_Usage"] = (i.Seconds_of_Use == 0).astype(int)
log["iran"] = (i.shape, i.Churn.mean(), n0 - len(i))
i.to_csv(f"{out}/iran_clean.csv", index=False)
for k, v in log.items(): print(k, v)
