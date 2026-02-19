# telecom_churn_analysis.py
# Minimal example for T-Mobile Business Analyst skills

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Simulated dataset
data = {
    "CustomerID": range(1, 11),
    "Contract": ["Month-to-Month", "One Year", "Two Year", "Month-to-Month", "Two Year",
                 "One Year", "Month-to-Month", "Two Year", "One Year", "Month-to-Month"],
    "MonthlyCharges": [70, 60, 80, 90, 75, 65, 85, 70, 60, 95],
    "Churn": ["Yes", "No", "No", "Yes", "No", "No", "Yes", "No", "No", "Yes"]
}

df = pd.DataFrame(data)

# Churn rate
churn_rate = df["Churn"].value_counts(normalize=True) * 100
print("Churn Rate (%):")
print(churn_rate)
print("\n")

# Churn by contract type
contract_churn = pd.crosstab(df["Contract"], df["Churn"], normalize="index") * 100
print("Churn by Contract Type (%):")
print(contract_churn)
print("\n")

# Average monthly charges by churn
avg_monthly = df.groupby("Churn")["MonthlyCharges"].mean()
print("Average Monthly Charges by Churn:")
print(avg_monthly)
print("\n")

# Plot churn by contract
plt.figure(figsize=(6,4))
sns.countplot(data=df, x="Contract", hue="Churn")
plt.title("Churn by Contract Type")
plt.tight_layout()
plt.savefig("churn_chart.png")
plt.show()
