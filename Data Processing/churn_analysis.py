import pandas as pd
subscriptions = pd.read_csv("subscriptions.csv")

#CHURN RATE this means annual percentage of subscribers who cancel their subscriptions
churn_rate = subscriptions['churned'].value_counts(normalize=True)*100
print('Overall Churn Rate (%):')
print(churn_rate)
churn_rate.to_csv("churn_rate.csv", index=False)

#CHURN RATE BY PLAN TYPE
churn_byplan=(
    subscriptions
    .groupby('plan')['churned']
    .value_counts(normalize=True)
    .unstack()*100
)
print('\nChurn Rate by Plan Type (%):')
print(churn_byplan)

#Revenue Lost Due to Churn
churned_mrr = subscriptions[subscriptions['churned'] == 'Yes']['mrr'].sum()
print('\n Churned Mrr(Monthly Recurring Revenue):',churned_mrr)
