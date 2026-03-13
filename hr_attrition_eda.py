"""
================================================================
PROJECT : HR Analytics - Employee Attrition & Salary EDA
Author  : Divin K Y | Data Analyst | Bengaluru
Tools   : Python, pandas, matplotlib, seaborn
Dataset : IBM HR Analytics (Kaggle - Public Dataset)
GitHub  : github.com/divin-k-y
================================================================
SKILLS DEMONSTRATED:
  Data Loading & Inspection | Null Handling | Data Type Cleaning
  Descriptive Statistics    | GroupBy & Aggregation
  Correlation Analysis      | Feature Engineering
  6 Business Visualisations | Insights & Recommendations
================================================================

SETUP: pip install pandas matplotlib seaborn

HOW TO GET THE DATASET:
  1. Go to: https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset
  2. Download WA_Fn-UseC_-HR-Employee-Attrition.csv
  3. Place it in the same folder as this script
================================================================
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# ── Style ────────────────────────────────────────────────────
sns.set_theme(style="whitegrid", palette="Blues_d")
plt.rcParams.update({'font.family': 'DejaVu Sans', 'figure.dpi': 120})
BLUE  = '#1A4F82'
RED   = '#C0392B'
GREEN = '#1E8449'

# ============================================================
# STEP 1 — LOAD & INSPECT
# ============================================================
print("=" * 60)
print("STEP 1: Loading & Inspecting Dataset")
print("=" * 60)

df = pd.read_csv('WA_Fn-UseC_-HR-Employee-Attrition.csv')

print(f"\nDataset Shape  : {df.shape[0]} rows × {df.shape[1]} columns")
print(f"Memory Usage   : {df.memory_usage(deep=True).sum() / 1024:.1f} KB")
print(f"\nColumn List:\n{df.columns.tolist()}")
print(f"\nData Types:\n{df.dtypes.value_counts()}")
print(f"\nNull Values:\n{df.isnull().sum()[df.isnull().sum() > 0]}")
print(f"\nAttrition Distribution:\n{df['Attrition'].value_counts()}")
print(f"Attrition Rate: {df['Attrition'].value_counts(normalize=True)['Yes']*100:.1f}%")


# ============================================================
# STEP 2 — DATA CLEANING & FEATURE ENGINEERING
# ============================================================
print("\n" + "=" * 60)
print("STEP 2: Data Cleaning & Feature Engineering")
print("=" * 60)

# Convert Attrition to binary
df['Attrition_Flag'] = df['Attrition'].map({'Yes': 1, 'No': 0})

# Age bands
df['Age_Band'] = pd.cut(df['Age'],
    bins=[17, 25, 30, 35, 40, 60],
    labels=['18-25', '26-30', '31-35', '36-40', '40+'])

# Salary bands (MonthlyIncome in USD)
df['Salary_Band'] = pd.cut(df['MonthlyIncome'],
    bins=[0, 3000, 6000, 10000, 20000],
    labels=['Low (<3K)', 'Mid (3-6K)', 'High (6-10K)', 'Very High (10K+)'])

# Tenure category
df['Tenure_Cat'] = pd.cut(df['YearsAtCompany'],
    bins=[-1, 1, 3, 7, 15, 40],
    labels=['<1 yr', '1-3 yrs', '3-7 yrs', '7-15 yrs', '15+ yrs'])

# Total compensation proxy
df['Total_Comp'] = df['MonthlyIncome'] * 12

print("\nFeature Engineering complete:")
print(f"  Age_Band    : {df['Age_Band'].value_counts().to_dict()}")
print(f"  Salary_Band : {df['Salary_Band'].value_counts().to_dict()}")
print(f"  Tenure_Cat  : {df['Tenure_Cat'].value_counts().to_dict()}")


# ============================================================
# STEP 3 — DESCRIPTIVE STATISTICS
# ============================================================
print("\n" + "=" * 60)
print("STEP 3: Descriptive Statistics")
print("=" * 60)

num_cols = ['Age', 'MonthlyIncome', 'YearsAtCompany',
            'JobSatisfaction', 'PerformanceRating', 'WorkLifeBalance']

print("\nKey Numerical Stats:")
print(df[num_cols].describe().round(2))

print("\nAttrition Rate by Department:")
dept_attr = df.groupby('Department')['Attrition_Flag'].agg(['mean', 'sum', 'count'])
dept_attr.columns = ['Attrition_Rate', 'Attrited', 'Total']
dept_attr['Attrition_Rate'] = (dept_attr['Attrition_Rate'] * 100).round(1)
print(dept_attr.sort_values('Attrition_Rate', ascending=False))

print("\nAttrition Rate by Job Role:")
role_attr = df.groupby('JobRole')['Attrition_Flag'].mean().sort_values(ascending=False)
print((role_attr * 100).round(1))

print("\nAvg Salary by Department:")
print(df.groupby('Department')['MonthlyIncome'].mean().round(0).sort_values(ascending=False))


# ============================================================
# STEP 4 — VISUALISATIONS (6 Charts)
# ============================================================
print("\n" + "=" * 60)
print("STEP 4: Generating Visualisations")
print("=" * 60)

fig, axes = plt.subplots(3, 2, figsize=(15, 16))
fig.suptitle('HR Analytics – Employee Attrition & Salary EDA\nAuthor: Divin K Y | Data Analyst | Bengaluru',
             fontsize=14, fontweight='bold', y=0.98, color=BLUE)

# ── Chart 1: Attrition Rate by Department ────────────────────
ax1 = axes[0, 0]
dept_data = df.groupby('Department')['Attrition_Flag'].mean().sort_values(ascending=False) * 100
bars = ax1.bar(dept_data.index, dept_data.values,
               color=[RED if v > 15 else BLUE for v in dept_data.values], edgecolor='white')
ax1.set_title('Attrition Rate by Department', fontweight='bold', color=BLUE)
ax1.set_ylabel('Attrition Rate (%)')
ax1.set_xlabel('')
for bar, val in zip(bars, dept_data.values):
    ax1.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.3,
             f'{val:.1f}%', ha='center', va='bottom', fontweight='bold', fontsize=10)
ax1.yaxis.set_major_formatter(mticker.PercentFormatter())


# ── Chart 2: Attrition Rate by Age Band ──────────────────────
ax2 = axes[0, 1]
age_attr = df.groupby('Age_Band', observed=True)['Attrition_Flag'].mean() * 100
bars2 = ax2.bar(age_attr.index.astype(str), age_attr.values,
                color=[RED if v > 20 else BLUE for v in age_attr.values], edgecolor='white')
ax2.set_title('Attrition Rate by Age Band', fontweight='bold', color=BLUE)
ax2.set_ylabel('Attrition Rate (%)')
ax2.set_xlabel('Age Band')
for bar, val in zip(bars2, age_attr.values):
    ax2.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.3,
             f'{val:.1f}%', ha='center', va='bottom', fontweight='bold', fontsize=10)
ax2.yaxis.set_major_formatter(mticker.PercentFormatter())


# ── Chart 3: Salary Distribution by Attrition ────────────────
ax3 = axes[1, 0]
attr_yes = df[df['Attrition'] == 'Yes']['MonthlyIncome']
attr_no  = df[df['Attrition'] == 'No']['MonthlyIncome']
ax3.hist(attr_yes, bins=25, alpha=0.7, color=RED,  label='Attrited',   edgecolor='white')
ax3.hist(attr_no,  bins=25, alpha=0.7, color=BLUE, label='Retained',   edgecolor='white')
ax3.axvline(attr_yes.mean(), color=RED,  linestyle='--', linewidth=2, label=f'Attrited Avg: ${attr_yes.mean():,.0f}')
ax3.axvline(attr_no.mean(),  color=BLUE, linestyle='--', linewidth=2, label=f'Retained Avg: ${attr_no.mean():,.0f}')
ax3.set_title('Monthly Salary Distribution — Attrited vs Retained', fontweight='bold', color=BLUE)
ax3.set_xlabel('Monthly Income (USD)')
ax3.set_ylabel('Employee Count')
ax3.legend(fontsize=8)


# ── Chart 4: Job Satisfaction vs Attrition ───────────────────
ax4 = axes[1, 1]
sat_attr = df.groupby('JobSatisfaction')['Attrition_Flag'].mean() * 100
ax4.bar(sat_attr.index.astype(str), sat_attr.values,
        color=[RED if v > 15 else BLUE for v in sat_attr.values], edgecolor='white')
ax4.set_title('Attrition Rate by Job Satisfaction Score', fontweight='bold', color=BLUE)
ax4.set_xlabel('Job Satisfaction (1=Low, 4=High)')
ax4.set_ylabel('Attrition Rate (%)')
ax4.yaxis.set_major_formatter(mticker.PercentFormatter())
for i, val in enumerate(sat_attr.values):
    ax4.text(i, val + 0.3, f'{val:.1f}%', ha='center', fontweight='bold', fontsize=10)


# ── Chart 5: Avg Salary by Job Role ──────────────────────────
ax5 = axes[2, 0]
role_sal = df.groupby('JobRole')['MonthlyIncome'].mean().sort_values()
ax5.barh(role_sal.index, role_sal.values, color=BLUE, edgecolor='white')
ax5.set_title('Average Monthly Salary by Job Role', fontweight='bold', color=BLUE)
ax5.set_xlabel('Average Monthly Income (USD)')
for i, val in enumerate(role_sal.values):
    ax5.text(val + 50, i, f'${val:,.0f}', va='center', fontsize=8)


# ── Chart 6: Tenure vs Attrition ─────────────────────────────
ax6 = axes[2, 1]
tenure_attr = df.groupby('Tenure_Cat', observed=True)['Attrition_Flag'].mean() * 100
bars6 = ax6.bar(tenure_attr.index.astype(str), tenure_attr.values,
                color=[RED if v > 15 else BLUE for v in tenure_attr.values], edgecolor='white')
ax6.set_title('Attrition Rate by Tenure', fontweight='bold', color=BLUE)
ax6.set_xlabel('Tenure at Company')
ax6.set_ylabel('Attrition Rate (%)')
ax6.yaxis.set_major_formatter(mticker.PercentFormatter())
for bar, val in zip(bars6, tenure_attr.values):
    ax6.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.3,
             f'{val:.1f}%', ha='center', va='bottom', fontweight='bold', fontsize=10)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig('hr_eda_dashboard.png', bbox_inches='tight', dpi=150)
plt.show()
print("\nChart saved as: hr_eda_dashboard.png")


# ============================================================
# STEP 5 — KEY INSIGHTS & RECOMMENDATIONS
# ============================================================
print("\n" + "=" * 60)
print("STEP 5: Key Insights & Business Recommendations")
print("=" * 60)

overall_attr = df['Attrition_Flag'].mean() * 100
high_attr_dept = dept_data.idxmax()
low_sat_attr   = (df[df['JobSatisfaction'] == 1]['Attrition_Flag'].mean() * 100)
high_sat_attr  = (df[df['JobSatisfaction'] == 4]['Attrition_Flag'].mean() * 100)
avg_sal_attrited = df[df['Attrition']=='Yes']['MonthlyIncome'].mean()
avg_sal_retained = df[df['Attrition']=='No']['MonthlyIncome'].mean()

print(f"""
📊 INSIGHT 1 — Overall Attrition
   Overall attrition rate: {overall_attr:.1f}%
   Highest attrition dept: {high_attr_dept}

📊 INSIGHT 2 — Age & Tenure Risk
   Employees aged 18-25 and with <1 year tenure show highest attrition.
   Early career employees are the most at-risk group.

📊 INSIGHT 3 — Salary Impact
   Attrited employees earned avg ${avg_sal_attrited:,.0f}/month
   Retained employees earned avg ${avg_sal_retained:,.0f}/month
   → Salary gap of ${avg_sal_retained - avg_sal_attrited:,.0f} suggests
     compensation is a key retention lever.

📊 INSIGHT 4 — Job Satisfaction
   Low satisfaction (1) attrition rate : {low_sat_attr:.1f}%
   High satisfaction (4) attrition rate: {high_sat_attr:.1f}%
   → Improving job satisfaction from 1→4 could reduce attrition by
     ~{low_sat_attr - high_sat_attr:.1f} percentage points.

✅ RECOMMENDATION 1: Target retention programmes for employees
   aged 18-30 in their first 3 years of tenure.

✅ RECOMMENDATION 2: Conduct salary benchmarking for Sales and
   HR departments where attrition is highest.

✅ RECOMMENDATION 3: Implement structured onboarding and
   mentoring for employees in first 12 months.

✅ RECOMMENDATION 4: Deploy employee satisfaction surveys
   quarterly and act on scores below 2.
""")

print("=" * 60)
print("EDA Complete. Charts saved. Ready to upload to GitHub.")
print("=" * 60)
