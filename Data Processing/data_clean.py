import pandas as pd
telco = pd.read_csv("Telco_customer_churn.csv")
ecommerce = pd.read_csv("E-commerce.csv")
support = pd.read_csv("support_tickets.csv")

def clean_columns(df):
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )
    return df

telco = clean_columns(telco)
ecommerce = clean_columns(ecommerce)
support = clean_columns(support)

#print(telco.columns)
#print(ecommerce.columns)
#print(support.columns)

accounts = telco[[
    "customerid",
    "gender",
    "senior_citizen",
    "partner",
    "dependents",
    "tenure_months"
]].rename(columns={
    "customerid": "account_id",
    "tenure_months": "account_tenure_months"
})
accounts.head()
#print(accounts.head())
subscriptions = telco[[
    "customerid",
    "contract",
    "monthly_charges",
    "payment_method",
    "churn_label"
]].rename(columns={
    "customerid": "account_id",
    "contract": "plan",
    "monthly_charges": "mrr",
    "churn_label": "churned"
})

subscriptions.head()
subscriptions.to_csv("subscriptions.csv", index=False)
print(accounts.shape)
print(subscriptions.shape)

#print(accounts["account_id"].nunique())
#print(subscriptions["account_id"].nunique())

events = ecommerce[[
    "customer_id",
    "items_purchased",
    "total_spend",
    "days_since_last_purchase"
]].rename(columns={
    "customer_id": "account_id"
})

# Simulate SaaS-style usage events
events["event_type"] = "product_usage"
events["event_time"] = pd.Timestamp.today()

events.head()
events.to_csv("events.csv", index=False)

support_tickets = support[[
    "ticket_id",
    "customer_email",
    "ticket_status",
    "ticket_priority",
    "first_response_time",
    "time_to_resolution",
    "customer_satisfaction_rating"
]].rename(columns={
    "customer_email": "account_contact"
})

support_tickets.head()
support_tickets.to_csv("support_tickets_cleaned.csv", index=False)
