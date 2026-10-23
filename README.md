# IKEA: Customer Analytics and RFM Segmentation

*An end-to-end data analytics project using SQL, Python, and Power BI*

**Author:** Arnav Andrew Vats | Aspiring Data Analyst | [LinkedIn](https://www.linkedin.com/in/arnav-andrew-vats/)

> **Key finding:** The *Champions* segment (25% of customers) generates **69% of revenue**, while **50.9%** of customers are flagged as churned under the project's fixed 90-day inactivity rule. The largest segment, *Needs Attention*, contributes only **3.8%** of revenue.

---

## Disclaimer

IKEA Gifting is a fictional business scenario created for this educational portfolio project. It is not affiliated with, endorsed by, or representative of the real IKEA corporation in any way. All figures in this project are derived from a public transactional dataset and do not reflect any real company's performance. IKEA branding in the dashboard is used for design and storytelling purposes only.

---

## Project Overview

This project simulates an analytics engagement for IKEA Gifting, a fictional UK-based online retailer of giftware and home décor. The goal was to take over one million raw transaction records and turn them into a decision-ready dashboard: define the business problem, clean the data in SQL, build the RFM and churn logic in Python, and deliver the insights through an interactive Power BI report.

## My Approach

- **Question first.** The project is guided by a Business Requirements Document that defines the business problem, questions, key definitions, and success criteria. Every analytical step traces back to one of those questions.
- **Simple, explainable logic.** Customers are scored 1 to 5 on Recency, Frequency, and Monetary value, and churn is a single fixed 90-day inactivity rule. This is easy to explain to a non-technical stakeholder. The trade-off is that it is a rule, not a predictive model, and predictive churn modeling is deliberately out of scope.
- **Honest about limits.** The source is real transactional data, so it carries real-world quirks such as cancellation invoices, missing values, and wholesale buyers mixed in with retail ones. Findings describe historical data, and suggested actions are recommendations, not measured outcomes.

## Business Problem

IKEA Gifting wants to identify its most valuable customers and reduce churn among customers at risk of leaving. Leadership has no structured view of customer value, so retention efforts are reactive instead of targeted.

**Stakeholders:** Marketing team, CRM & Retention team, and Business Leadership.

## Business Questions Answered

1. Who are the most valuable customers, and how much revenue do they contribute?
2. Which customers have gone quiet and are at risk of churning?
3. How do customer value and retention trend across months, quarters, and years?
4. How do customer value and churn differ across countries?
5. What concrete actions should the business take for each customer segment?

## Customer Segments

**Recency (R):** days since a customer's most recent purchase. **Frequency (F):** number of distinct purchase transactions. **Monetary (M):** total revenue from the customer. **Churn:** flagged when there is no recorded purchase in the trailing 90 days.

| Segment | Description | Customers | % of Revenue | Avg. Customer Value |
|---|---|---:|---:|---:|
| Champions | High recency, frequency, and spend | 1,473 | **69.0%** | £8,143 |
| Loyal | Consistent buyers with moderate-to-high value | 1,232 | 14.6% | £2,063 |
| At Risk | Previously valuable, recently inactive | 823 | 9.1% | £1,930 |
| Needs Attention | Moderate recency, low frequency | 1,529 | 3.8% | £429 |
| New | Recent customers without repeat purchases yet | 442 | 2.3% | £887 |
| Lost | No meaningful activity for an extended period | 382 | 1.2% | £530 |
| **Total** | | **5,881** | **100%** | **£2,954** |

*Total revenue across all segments is **£17.4M** (the dashboard's KPI card shows it rounded). Average customer value is total revenue divided by total customers. Revenue shares are derived from the dashboard's segment performance table.*
---
## Key Findings

- **Revenue is concentrated in Champions.** 1,473 customers (25.0% of the base) generate £12.0M, or 69.0% of revenue, at £8,143 per customer, nearly 4x the next-best segment.
- **Churn risk is significant.** 50.9% of customers are flagged as churned under the project's fixed 90-day inactivity rule.
- **The largest segment is one of the least valuable.** Needs Attention has the most customers (1,529, 26%) but contributes only 3.8% of revenue.
- **At Risk is the best win-back target.** These 823 customers have very low recency (1.71) but frequency and monetary scores (3.92 / 3.85) close to Loyal customers, and hold £1.6M (9.1%) of revenue.
- **Customer value varies sharply by segment**, from £429 (Needs Attention) to £8,143 (Champions).
- **Revenue peaks in Q4.** Q4 delivers £6.2M, about 36% of total revenue, versus £3.4M in Q1, consistent with a gifting-focused product range.
- **The business is UK-centric.** The UK accounts for 91% of customers and 83% of revenue. A few smaller markets show very high value per customer (EIRE £123K, Singapore £25.3K, Netherlands £25.2K), but these rest on small customer bases, so treat them as leads, not rankings.

## Suggested Actions

| Segment | Priority | Suggested action |
|---|---|---|
| Champions | Protect | Early access, loyalty perks, and account management for the largest accounts |
| Loyal | Grow | Cross-sell and upsell toward Champion behaviour |
| At Risk | **Win back first** | Personalized reactivation before these customers lapse completely |
| Needs Attention | Qualify | Low-cost automated nurture to lift purchase frequency |
| New | Convert | Onboarding and second-purchase incentives |
| Lost | Low priority | Low-cost reactivation tests only |

*These are suggestions based on the segment results, not measured outcomes. The project does not claim any action will improve revenue or reduce churn.*

---

## Data Source

**Online Retail II**, [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/502/online+retail+ii), donated by Daqing Chen. A real, anonymized transactional dataset from a UK-based, non-store online retailer that mainly sells all-occasion giftware, covering **1 December 2009 to 9 December 2011**. It contains **1,067,371 transaction records**, with unit prices in pounds sterling (£). Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0). A backup copy is included in this repository with attribution.

Citation:
Chen, D. (2012). *Online Retail II* [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5CG6D
---
## Tools and Tech Stack

| Tool | Purpose in this project |
|---|---|
| SQL | Data extraction, cleaning, deduplication, and preparation |
| Python (Pandas) | RFM calculation, customer scoring, segmentation logic, and churn flagging |
| Power BI Desktop | Three-page interactive dashboard |
| DAX | Measures for the KPI cards (customers, revenue, churned %, average customer value) |
| Power Query | Data transformation and preparation |
---
## Core Concepts Demonstrated

- **RFM Analysis:** scoring customers on Recency, Frequency, and Monetary value so customer worth is comparable.
- **Customer Segmentation:** translating RFM scores into six business-meaningful groups.
- **Churn Definition and Flagging:** applying a fixed 90-day inactivity threshold to identify customers at risk of lapsing.
- **Data Cleaning:** preparing a large raw transaction dataset for customer-level analysis.
- **Interactive BI Design:** slicers, toggles, and multi-page navigation in Power BI.
- **Business Storytelling:** turning segment results into suggested actions for Marketing and CRM teams.
---
## Project Workflow

**Step 1: Business Requirements Document.** Defined scope, business questions, key definitions, and success criteria.

**Step 2: SQL, Data Cleaning.** Cleaned, deduplicated, and prepared the raw transaction data into an analysis-ready dataset.

**Step 3: Python, RFM Segmentation.** Calculated Recency, Frequency, and Monetary value per customer, scored each dimension on a 1 to 5 scale, assigned each of the 5,881 customers to one of six segments, and added the 90-day churn flag.

**Step 4: Power BI, Dashboard and Findings.** Loaded the customer-level results, built a three-page interactive report, and interpreted the results into suggested actions.

---
## Dashboard Structure

**Page 1: Home.** Project title, navigation to the two report pages, and a glossary defining Recency, Frequency, Monetary, and Churned %.

![Home and navigation]
<img width="768" height="430" alt="1" src="https://github.com/user-attachments/assets/cda3333f-9d66-4623-a45b-0de765a57480" />

**Page 2: Business Overview.** KPI cards for total customers, total revenue, churned %, and average customer value, with a **Revenue / Customer** toggle, segment breakdowns, and month, quarter, and year trends. Filterable by month, quarter, year, country, segment, and churn status.
[Business Overview, Revenue view]
<img width="703" height="436" alt="2" src="https://github.com/user-attachments/assets/7e6c8626-86cc-4092-ad8d-967fca19d526" />

[Business Overview, Customer view]
<img width="700" height="437" alt="3" src="https://github.com/user-attachments/assets/bd9a21cc-5b55-4592-b9d2-94cca5bf8328" />

**Page 3: RFM Analysis.** A **Segment / Country** toggle. The segment view shows a performance summary table (customers, revenue, average R, F, M scores) and average customer value by segment. The country view shows the same table by country and the top 5 countries by average customer value. Both views trend churned % by month, quarter, and year.

[RFM Analysis, Segment view] 

<img width="698" height="439" alt="4" src="https://github.com/user-attachments/assets/78307bba-2d7a-4f60-9c70-b512772610dc" />

[RFM Analysis, Country view]

<img width="699" height="437" alt="5" src="https://github.com/user-attachments/assets/cfc5d82d-8fc4-4577-b3b2-0d4e7d43da5d" />


---
## Assumptions and Limitations

- **Fixed churn threshold:** churn is a 90-day inactivity rule, not a statistically derived cutoff or a predictive model.
- **Wholesale and retail are not separated** unless the data clearly distinguishes them, so some values, especially in small markets, may be inflated by bulk buyers.
- **Historical data only:** the analysis does not account for external factors such as promotional calendars.
- **Yearly comparisons are not like-for-like:** the data starts on 1 December 2009 (so 2009 is one month) and ends on 9 December 2011.
- **Period views are not additive:** a customer is counted in every month, quarter, or year in which they were active, so period counts do not sum to 5,881.
- **Churn over time:** churn is a single customer-level flag, so the churned % by period charts show how that flag is distributed, not a true period-over-period churn rate.
