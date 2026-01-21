# SaaS Customer Churn Analytics & Executive Insight System

## Overview

- Built an **end-to-end SaaS analytics system** focused on converting churn metrics into **actionable executive recommendations**
- Combines **data engineering**, **business intelligence**, and **large language models (LLMs)**
- Transforms raw customer data into structured analytics, executive dashboards, and **decision-ready insights**
- Designed to reflect **real-world SaaS analytics and leadership reporting workflows**

## Business Problem

- SaaS companies can measure churn and revenue metrics, but often struggle to:
  - Translate dashboards into **clear actions**
  - Prioritize **retention strategies**
  - Communicate insights effectively to leadership
- Most BI systems explain *what* happened, but not **how the business should respond**

## Solution Approach

- Built a layered analytics system where:
  - Python-based data processing and dashboards provide analytical context
  - An LLM-driven insight layer generates **clear, prioritized recommendations**
- Dashboards support decision-making, while recommendations guide **business action**

## Recommendation Engine (Key Highlight)

The system automatically generates **executive-level recommendations** based on churn, revenue, and engagement analysis.

### What the Recommendations Provide

- Clear articulation of **what is happening** in the business  
- Explanation of **why churn is occurring**  
- Actionable, leadership-focused recommendations to address churn and revenue risk  

## Example Executive Insight (LLM-Generated Output)

**Executive Summary**

- The executive dashboard indicates a **high overall churn rate of 73.46%**, placing a significant amount of **monthly recurring revenue ($139,130.85) at risk**
- High-risk engagement segments show that customers with **medium and low engagement** are the primary contributors to churn
- This represents a **critical business risk** that requires immediate leadership attention

**What Is Happening**

- A substantial portion of customers are canceling subscriptions, resulting in significant revenue loss
- Customers with lower engagement levels are disproportionately represented among churned users

**Why Churn Is Occurring**

- **Insufficient engagement:** Customers who do not actively use the product are more likely to churn  
- **Low perceived value:** Some customers may not clearly understand or experience the product’s value  

**Recommended Actions for Leadership**

- **Improve engagement strategies:** Launch targeted re-engagement campaigns for medium- and low-engagement customers, emphasizing key product value and use cases  
- **Enhance customer experience:** Identify gaps in product usability and customer support to improve satisfaction  
- **Analyze churn drivers:** Perform deeper analysis across product usage, pricing, and support interactions  
- **Implement retention initiatives:** Introduce loyalty programs, personalized support, or retention-focused offers to reduce churn  

This output demonstrates how the system converts dashboard metrics into **clear, executive-ready recommendations**.

## Key Features

- End-to-end data pipeline using **Python and Pandas**
- Customer churn and engagement analysis
- Customer health scoring and segmentation
- Executive **Power BI dashboard** for analytical context
- **LLM-based automated recommendation and insight generation**
- Clean, modular, production-style project structure

## Architecture

- **Raw CSV Data**  
- **Python Data Processing (Pandas)**  
- **Analytical Metrics & Aggregations**  
- **Power BI Executive Dashboard**  
- **LLM-Based Recommendation & Insight Layer**  

## Dashboard Highlights

The Power BI dashboard provides supporting analytics, including:

- Overall churn rate  
- Monthly Recurring Revenue (MRR) at risk  
- Churn by subscription plan  
- Churn by payment method  
- Customer engagement distribution  
- Customer health by engagement segment  

## Tech Stack

- **Python** – Data processing and analytics logic  
- **Pandas** – Data transformation and metric computation  
- **Power BI** – Executive dashboard and KPI visualization  
- **LLM (Groq / Llama)** – Automated executive recommendations  
- **Git & GitHub** – Version control and project management  

## Business Impact

- Moves analytics beyond descriptive reporting to **action-oriented decision support**
- Helps leadership:
  - Identify churn drivers faster  
  - Quantify revenue at risk  
  - Prioritize retention initiatives  
- Reduces manual effort in interpreting dashboards and drafting executive recommendations

## How to Run

1. Clone the repository  
2. Add your API key to a `.env` file  
3. Install required dependencies  
4. Run the LLM insight pipeline  
