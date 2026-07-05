import pandas as pd

# Load the dataset
df = pd.read_csv("Placement_Data_Full_Class.csv")

# See first 5 rows
print(df.head())

# Shape of data
print("\nShape:", df.shape)

# All column names
print("\nColumns:", df.columns.tolist())
# How many students placed vs not placed
print("\nPlacement Count:")
print(df['status'].value_counts())

# Average salary of placed students
placed = df[df['status'] == 'Placed']
print("\nAverage Salary (Placed students):")
print(round(placed['salary'].mean(), 2))

# Placement rate
total = len(df)
placed_count = len(placed)
rate = round((placed_count / total) * 100, 2)
print(f"\nPlacement Rate: {rate}%")
# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing salary with 0 (unplaced students have no salary)
df['salary'] = df['salary'].fillna(0)

# Verify no missing values remain
print("\nMissing Values After Cleaning:")
print(df.isnull().sum().sum(), "missing values remaining")

# Basic statistics of salary
print("\nSalary Statistics:")
print(df[df['salary'] > 0]['salary'].describe().round(2))
# Placement rate by gender
print("\nPlacement Rate by Gender:")
gender_placement = df.groupby('gender')['status'].value_counts(normalize=True).mul(100).round(2)
print(gender_placement)

# Average salary by specialisation
print("\nAverage Salary by Specialisation:")
spec_salary = df[df['salary'] > 0].groupby('specialisation')['salary'].mean().round(2)
print(spec_salary)

# Placement rate by work experience
print("\nPlacement Rate by Work Experience:")
work_placement = df.groupby('workex')['status'].value_counts(normalize=True).mul(100).round(2)
print(work_placement)

# Average salary by degree type
print("\nAverage Salary by Degree Type:")
degree_salary = df[df['salary'] > 0].groupby('degree_t')['salary'].mean().round(2)
print(degree_salary)
import matplotlib.pyplot as plt

# Chart 1 — Placement Status Pie Chart
plt.figure(figsize=(6, 6))
status_counts = df['status'].value_counts()
plt.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%',
        colors=['#378ADD', '#E24B4A'])
plt.title('Placement Status Distribution')
plt.savefig('chart1_placement_status.png')
plt.show()
print("Chart 1 saved.")
# Chart 2 — Average Salary by Specialisation
plt.figure(figsize=(8, 5))
spec_salary.plot(kind='bar', color=['#378ADD', '#5DCAA5'])
plt.title('Average Salary by Specialisation')
plt.xlabel('Specialisation')
plt.ylabel('Average Salary (₹)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('chart2_salary_specialisation.png')
plt.show()
print("Chart 2 saved.")

# Chart 3 — Work Experience vs Placement
plt.figure(figsize=(8, 5))
workex_data = df.groupby('workex')['status'].value_counts().unstack()
workex_data.plot(kind='bar', color=['#E24B4A', '#378ADD'])
plt.title('Work Experience vs Placement')
plt.xlabel('Work Experience')
plt.ylabel('Number of Students')
plt.xticks(rotation=0)
plt.legend(['Not Placed', 'Placed'])
plt.tight_layout()
plt.savefig('chart3_workex_placement.png')
plt.show()
print("Chart 3 saved.")

# Chart 4 — Average Salary by Degree Type
plt.figure(figsize=(8, 5))
degree_salary.plot(kind='bar', color=['#7F77DD', '#5DCAA5', '#EF9F27'])
plt.title('Average Salary by Degree Type')
plt.xlabel('Degree Type')
plt.ylabel('Average Salary (₹)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('chart4_salary_degree.png')
plt.show()
print("Chart 4 saved.")

# Chart 5 — SSC Score vs MBA Score colored by placement
import matplotlib.pyplot as plt

placed_df = df[df['status'] == 'Placed']
not_placed_df = df[df['status'] == 'Not Placed']

plt.figure(figsize=(8, 5))
plt.scatter(placed_df['ssc_p'], placed_df['mba_p'], 
            color='#378ADD', label='Placed', alpha=0.6)
plt.scatter(not_placed_df['ssc_p'], not_placed_df['mba_p'], 
            color='#E24B4A', label='Not Placed', alpha=0.6)
plt.title('SSC Score vs MBA Score by Placement Status')
plt.xlabel('SSC Score (%)')
plt.ylabel('MBA Score (%)')
plt.legend()
plt.tight_layout()
plt.savefig('chart5_ssc_vs_mba.png')
plt.show()
print("Chart 5 saved.")

# Auto-generated Insights
print("\n" + "="*50)
print("       PLACEMENT INSIGHTS SUMMARY")
print("="*50)

total = len(df)
placed_count = len(df[df['status'] == 'Placed'])
not_placed_count = len(df[df['status'] == 'Not Placed'])
avg_salary = df[df['salary'] > 0]['salary'].mean()
max_salary = df['salary'].max()
min_salary = df[df['salary'] > 0]['salary'].min()

workex_placed = len(df[(df['workex'] == 'Yes') & (df['status'] == 'Placed')])
workex_total = len(df[df['workex'] == 'Yes'])
workex_rate = round((workex_placed / workex_total) * 100, 2)

no_workex_placed = len(df[(df['workex'] == 'No') & (df['status'] == 'Placed')])
no_workex_total = len(df[df['workex'] == 'No'])
no_workex_rate = round((no_workex_placed / no_workex_total) * 100, 2)

top_spec = df[df['salary'] > 0].groupby('specialisation')['salary'].mean().idxmax()
top_degree = df[df['salary'] > 0].groupby('degree_t')['salary'].mean().idxmax()

print(f"1. Total students analyzed: {total}")
print(f"2. Placement rate: {round((placed_count/total)*100, 2)}%")
print(f"3. Average salary of placed students: Rs {round(avg_salary, 2)}")
print(f"4. Highest salary offered: Rs {max_salary}")
print(f"5. Lowest salary offered: Rs {min_salary}")
print(f"6. Placement rate WITH work experience: {workex_rate}%")
print(f"7. Placement rate WITHOUT work experience: {no_workex_rate}%")
print(f"8. Best paying specialisation: {top_spec}")
print(f"9. Best paying degree type: {top_degree}")
print(f"10. Work experience advantage: {round(workex_rate - no_workex_rate, 2)}% higher placement rate")
print("="*50)

from matplotlib.backends.backend_pdf import PdfPages

print("\nGenerating PDF report...")

with PdfPages('Placement_Analysis_Report.pdf') as pdf:
    # Page 1 — Pie Chart
    fig, ax = plt.subplots(figsize=(8, 6))
    status_counts = df['status'].value_counts()
    ax.pie(status_counts, labels=status_counts.index, 
           autopct='%1.1f%%', colors=['#378ADD', '#E24B4A'])
    ax.set_title('Placement Status Distribution', fontsize=14)
    pdf.savefig(fig)
    plt.close()

    # Page 2 — Salary by Specialisation
    fig, ax = plt.subplots(figsize=(8, 6))
    spec_salary.plot(kind='bar', color=['#378ADD', '#5DCAA5'], ax=ax)
    ax.set_title('Average Salary by Specialisation', fontsize=14)
    ax.set_xlabel('Specialisation')
    ax.set_ylabel('Average Salary (₹)')
    ax.tick_params(axis='x', rotation=0)
    pdf.savefig(fig)
    plt.close()

    # Page 3 — Work Experience vs Placement
    fig, ax = plt.subplots(figsize=(8, 6))
    workex_data = df.groupby('workex')['status'].value_counts().unstack()
    workex_data.plot(kind='bar', color=['#E24B4A', '#378ADD'], ax=ax)
    ax.set_title('Work Experience vs Placement', fontsize=14)
    ax.set_xlabel('Work Experience')
    ax.set_ylabel('Number of Students')
    ax.tick_params(axis='x', rotation=0)
    ax.legend(['Not Placed', 'Placed'])
    pdf.savefig(fig)
    plt.close()

    # Page 4 — Salary by Degree
    fig, ax = plt.subplots(figsize=(8, 6))
    degree_salary.plot(kind='bar', 
                       color=['#7F77DD', '#5DCAA5', '#EF9F27'], ax=ax)
    ax.set_title('Average Salary by Degree Type', fontsize=14)
    ax.set_xlabel('Degree Type')
    ax.set_ylabel('Average Salary (₹)')
    ax.tick_params(axis='x', rotation=0)
    pdf.savefig(fig)
    plt.close()

    # Page 5 — Insights Text
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.axis('off')
    insights = f"""
    PLACEMENT INSIGHTS SUMMARY
    {'='*45}
    
    1.  Total students analyzed: {total}
    2.  Placement rate: {round((placed_count/total)*100, 2)}%
    3.  Average salary (placed): Rs {round(avg_salary, 2)}
    4.  Highest salary offered: Rs {max_salary}
    5.  Lowest salary offered: Rs {min_salary}
    6.  Placement rate WITH work experience: {workex_rate}%
    7.  Placement rate WITHOUT work experience: {no_workex_rate}%
    8.  Best paying specialisation: {top_spec}
    9.  Best paying degree type: {top_degree}
    10. Work experience advantage: {round(workex_rate - no_workex_rate, 2)}%
    """
    ax.text(0.1, 0.5, insights, transform=ax.transAxes,
            fontsize=12, verticalalignment='center',
            fontfamily='monospace')
    pdf.savefig(fig)
    plt.close()

print("PDF Report saved as 'Placement_Analysis_Report.pdf'")
print("\nProject Complete!")