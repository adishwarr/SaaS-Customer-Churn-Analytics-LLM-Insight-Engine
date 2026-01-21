import pandas as pd
import llmclient


def generate_executive_insight():
    # Load dashboard data
    churn = pd.read_csv("churn_rate.csv")
    subscriptions = pd.read_csv("subscriptions.csv")
    engagement = pd.read_csv("segment_health_summary.csv")

    # Key metrics
    churn_rate = float(churn.iloc[0, 0])
    mrr_at_risk = subscriptions.loc[
        subscriptions["churned"] == "Yes", "mrr"
    ].sum()

    red_segments = engagement[engagement["health_status"] == "Red"]

    # Prompt for LLM
    prompt = f"""
You are analyzing a SaaS executive dashboard.

Key metrics:
- Overall churn rate: {churn_rate:.2f}%
- Monthly recurring revenue at risk: {mrr_at_risk:,.2f}

High-risk engagement segments:
{red_segments[['engagement_level', 'base_health_score']].to_string(index=False)}

Explain clearly:
1. What is happening
2. Why churn is occurring
3. What actions leadership should take

Write a concise executive-level summary.
"""

    return llmclient.ask_llm(prompt)


if __name__ == "__main__":
    insight = generate_executive_insight()
    print("\n📊 EXECUTIVE DASHBOARD INSIGHT\n")
    print(insight)

insight = generate_executive_insight()

with open("executive_dashboard_insight.txt", "w", encoding="utf-8") as f:
    f.write(insight)

print("\n📊 EXECUTIVE DASHBOARD INSIGHT\n")
print(insight)
