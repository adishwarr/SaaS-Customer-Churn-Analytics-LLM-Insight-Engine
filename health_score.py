import pandas as pd

subscriptions = pd.read_csv("subscriptions.csv")
usage_metrics = pd.read_csv("usage_metrics.csv")

print("Subscriptions shape:", subscriptions.shape)
print("Usage metrics shape:", usage_metrics.shape)

# 1. ENGAGEMENT DISTRIBUTION:

engagement_distribution = (
    usage_metrics["engagement_level"]
    .value_counts(normalize=True)
    .reset_index()
)

engagement_distribution.columns = [
    "engagement_level",
    "usage_percentage"
]

print("\nEngagement Level Distribution (%):")
print(engagement_distribution)


# 2. OVERALL CHURN RATE
# (Recomputed here — scripts are isolated)

churn_rate = (
    subscriptions["churned"]
    .value_counts(normalize=True)
    .reset_index()
)

churn_rate.columns = ["churn_status", "percentage"]

overall_churn = churn_rate.loc[
    churn_rate["churn_status"] == "Yes",
    "percentage"
].values[0]

print("\nOverall Churn Rate (%):", overall_churn)



# 3. SEGMENT-LEVEL HEALTH SCORE MODEL: out of how many costumers are in low med and high engagement level
# ======================================

base_health_map = {
    "High": 0.8,
    "Medium": 0.5,
    "Low": 0.2
}

engagement_distribution["base_health_score"] = (
    engagement_distribution["engagement_level"]
    .map(base_health_map)
)

# Adjust health score by churn pressure
engagement_distribution["adjusted_health_score"] = (
    engagement_distribution["base_health_score"]
    * (1 - overall_churn)
)

# 4. HEALTH STATUS LABELS

engagement_distribution["health_status"] = pd.cut(
    engagement_distribution["adjusted_health_score"],
    bins=[-0.01, 0.4, 0.7, 1.0],
    labels=["Red", "Yellow", "Green"]
)

print("\nSegment-Level Health Summary:")
print(engagement_distribution)


# 5. SAVE FINAL OUTPUT

engagement_distribution.to_csv(
    "segment_health_summary.csv",
    index=False
)

print("\n segment_health_summary.csv saved successfully.")
