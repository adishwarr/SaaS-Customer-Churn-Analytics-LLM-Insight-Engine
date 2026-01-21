import pandas as pd
events = pd.read_csv("events.csv")
subscriptions = pd.read_csv("subscriptions.csv")

print('Events Shape',events.shape)
print('Subscriptions.Shape',subscriptions.shape)

#USAGE BY EACH ACCOUNT
usage_per_account = (
    events
    .groupby('account_id')['items_purchased']
    .sum()
    .reset_index(name='total usage')
)
print('\nUsage per Account:',usage_per_account.head())

#USAGE SUMMARY
usage_summary=usage_per_account['total usage'].describe()
print('\nUsage Summary:',usage_summary)


# ENGAGEMENT SEGMENTATION

usage_per_account["engagement_level"] = pd.cut(
    usage_per_account["total usage"],
    bins=[-1, usage_summary["25%"], usage_summary["75%"], usage_summary["max"]],
    labels=["Low", "Medium", "High"]
)

print("\nEngagement level distribution:")
print(usage_per_account["engagement_level"].value_counts())

#  SAVING USAGE METRICS FOR NEXT STEP

usage_per_account.to_csv(
    "usage_metrics.csv",
    index=False
)



