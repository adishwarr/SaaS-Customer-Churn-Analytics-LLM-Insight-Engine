import pandas as pd
import llmclient


def generate_executive_insight():
    churn = pd.read_csv("churn_rate.csv")
    subscriptions = pd.read_csv("subscriptions.csv")
    engagement = pd.read_csv("segment_health_summary.csv")

    churn_rate = float(churn.iloc[0, 0])
    mrr_at_risk = subscriptions.loc[
        subscriptions["churned"] == "Yes", "mrr"
    ].sum()

    red_segments = engagement[engagement["health_status"] == "Red"]

    prompt = f"""
You are analyzing a SaaS executive dashboard.

Key metrics:
- Overall churn rate: {churn_rate:.2f}%
- Monthly recurring revenue at risk: {mrr_at_risk:,.2f}

High-risk engagement segments:
{red_segments[['engagement_level', 'base_health_score']].to_string(index=False)}

Explain:
1. What is happening
2. Why churn is occurring
3. What actions leadership should take

Write a concise executive summary.
"""

    return llmclient.ask_llm(prompt)
