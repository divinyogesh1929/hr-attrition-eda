# 🐍 HR Analytics — Attrition & Salary EDA (Python Project)

**Author:** Divin K Y | Data Analyst | Bengaluru  
**Tools:** Python, pandas, matplotlib, seaborn  
**Dataset:** IBM HR Analytics Attrition Dataset (Kaggle — Public)

---

## 🎯 Project Objective

Perform end-to-end Exploratory Data Analysis (EDA) on IBM's HR dataset (1,470 employees) to identify key drivers of employee attrition and salary patterns — and deliver actionable business recommendations for HR leadership.

---

## 📁 Files

| File | Description |
|------|-------------|
| `hr_attrition_eda.py` | Full EDA script — data cleaning, analysis, 6 visualisations, insights |
| `hr_eda_dashboard.png` | Output dashboard — 6 charts |

---

## 📊 Analysis Performed

| Step | What Was Done |
|------|---------------|
| Data Loading & Inspection | Shape, dtypes, null check, value counts |
| Data Cleaning | Type conversion, null handling |
| Feature Engineering | Age bands, salary bands, tenure categories, total comp |
| Descriptive Statistics | Mean, median, std, percentiles per key variable |
| GroupBy Analysis | Attrition rate by dept, role, age, tenure, satisfaction |
| 6 Visualisations | Bar charts, histograms, horizontal bars |
| Business Insights | 4 insights + 4 actionable recommendations |

---

## 📈 6 Charts Generated

1. **Attrition Rate by Department** — which team loses most people?
2. **Attrition Rate by Age Band** — which age group is most at risk?
3. **Salary Distribution: Attrited vs Retained** — does pay drive exits?
4. **Job Satisfaction vs Attrition** — satisfaction's impact on retention
5. **Average Salary by Job Role** — compensation benchmarking
6. **Attrition Rate by Tenure** — when do employees leave?

---

## 💡 Key Insights

- Overall attrition rate: **16.1%** — above healthy 10–12% benchmark
- **Sales department** has the highest attrition (~20%)
- Employees with **job satisfaction score of 1** have 2.5× more attrition than score 4
- **Attrited employees earn $2,000/month less** on average than retained employees
- **<1 year tenure** employees are highest-risk group for exits

---

## ✅ Business Recommendations

1. Target retention programmes for employees aged 18–30 in their first 3 years
2. Conduct salary benchmarking for Sales — compensation gap is a clear risk
3. Implement structured onboarding & mentoring for first 12 months
4. Deploy quarterly satisfaction surveys and act on scores below 2

---

## 🚀 How to Run

```bash
# 1. Install dependencies
pip install pandas matplotlib seaborn

# 2. Download dataset from Kaggle:
# https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset
# Save as: WA_Fn-UseC_-HR-Employee-Attrition.csv

# 3. Run
python hr_attrition_eda.py
```

---

## 📬 Connect

- **LinkedIn:** linkedin.com/in/divin-k-y
- **Email:** divinyogesh10@gmail.com
- **Location:** Bengaluru, Karnataka | Immediate Joiner
