# -*- coding: utf-8 -*-
"""Copy of Python Project - Employee Attrition.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CVYfPEB_Kx_KPTyxxml9sOn5IvxRNkf1

# Analyse Employee Attrition

## Task

Uncover the factors that lead to employee attrition.

1. Have a look at the variables, understand what they are.
2. Which variables are associated with attrition? For which groups of employees
does this association hold (`Department`, `JobLevel`, etc.)? Formulate several hypotheses.
3. Explore each hypothesis.
    - Make plots and/or compute statistics.
    - Write a short conclusion, refer to the justifications you found in the data.

## Dataset

_Source: https://www.kaggle.com/datasets/whenamancodes/hr-employee-attrition_

This is a fictional data set created by IBM data scientists. It contains data about employees in a company.

Encoding of some of the columns:

```
Education
1 'Below College'
2 'College'
3 'Bachelor'
4 'Master'
5 'Doctor'

EnvironmentSatisfaction
1 'Low'
2 'Medium'
3 'High'
4 'Very High'

JobInvolvement
1 'Low'
2 'Medium'
3 'High'
4 'Very High'

JobSatisfaction
1 'Low'
2 'Medium'
3 'High'
4 'Very High'

PerformanceRating
1 'Low'
2 'Good'
3 'Excellent'
4 'Outstanding'

RelationshipSatisfaction
1 'Low'
2 'Medium'
3 'High'
4 'Very High'

WorkLifeBalance
1 'Bad'
2 'Good'
3 'Better'
4 'Best'
```

## Analysis
"""

import pandas as pd
import seaborn as sns

# From https://drive.google.com/file/d/1TGVkYpXg9efkuh-N3UCaahBtCQhs65vy/view
df = pd.read_csv(
    "https://drive.google.com/uc?id=1TGVkYpXg9efkuh-N3UCaahBtCQhs65vy",
    true_values=["Yes"],
    false_values=["No"],
)
df.shape

df.info()
#this will help to know the overview of the data's structure.

df.describe()
#will give an overview of the central tendency, dispersion, and distribution of your data and help to quickly understand the distribution of values, identify potential outliers and get a sense of the data's central tendency and variability.

df.columns
#will retrieve the column names

df.head()
#will display the first five rows of the DataFrame

df.Attrition.unique()
# it will show you the unique values present in the column 'attrition'

attrition_counts = df['Attrition'].value_counts()
# It calculates how many employees have "Attrition" set to 'True' and how many have it set to 'False'.
print(attrition_counts)

import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(20,10))
sns.heatmap(df.corr(method="kendall"), annot=True, fmt=".3f", ax=ax);

# Correlation Coeficient Range [-1 - 1]

#-1 is perfectly negative Correlation
#1 is perfect positive correlation

df_corr = df.corr(method='pearson')
df_corr

df.Department.unique()
# is used to retrieve the unique values of the department column

#Query: Get the maximum years at the company for any employee.
max_years_at_company = df['YearsAtCompany'].max()
print("Maximum Years at the Company: {}".format(max_years_at_company))

#Find the department with the highest average monthly income among employees with more than 5 years of experience at the company.
df.query("YearsAtCompany > 5").groupby('Department')['MonthlyIncome'].mean().idxmax()

#print(cars.query('Year >= 2016 & Make == "Ford"').shape)

df.query("Age > 40 & Department =='Sales'")
#contains the row for the employees who are in the 'Sales' department and has an age greater than 40.

#Hypothesis 1:Employees who live farther from work are more likely to experience attrition.
sns.boxplot(data=df, x='Attrition', y='DistanceFromHome')
plt.title('Distance from Home by Attrition')
plt.xlabel('Attrition')
plt.ylabel('Distance from Home')
plt.show()

#Conclusion: the data supports the hypothesis that employees who live farther from work are more likely to experience attrition. The findings emphasize the importance of considering the impact of commute distance when addressing attrition within the organization.

#Hypothesis 2 :Employees with fewer years at the company are more likely to experience attrition.
sns.boxplot(data=df, x='Attrition', y='YearsAtCompany')
plt.title('Attrition by Years at Company')
plt.show()
# The analysis reveals that employees with fewer years at the company are more likely to experience attrition. The data indicates that employees with fewer years at the company are more prone to leave suggesting that employee tenure is associated with attrition.

#Hypothesis 3: Employees at lower job levels are more likely to experience attrition.
joblevel_attrition = df.groupby(['JobLevel', 'Attrition']).size().unstack()
joblevel_attrition.plot(kind='bar', stacked=True)
plt.title('Attrition by Job Level')
plt.xlabel('Job Level')
plt.ylabel('Count')
plt.show()
#Conclusion:The analysis suggests that employees at lower job levels such as JobLevel 1 are more likely to experience attrition. There is a noticeable relationship between job level and attrition, with lower job levels having higher attrition rates.

#Hypotheis 4:Single employees are more likely to experience attrition compared to married or divorced employees.
marital_attrition = df.groupby(['MaritalStatus', 'Attrition']).size().unstack()
marital_attrition.plot(kind='bar', stacked=True)
plt.title('Attrition by Marital Status')
plt.xlabel('Marital Status')
plt.ylabel('Count')
plt.show()
#Conclusion : The analysis indicates that single employees have a slightly higher attrition rate compared to married or divorced employees. Marital status may play a minor role in attrition.

#Hypotheis 5:Employees in certain job roles are more likely to experience attrition.
jobrole_attrition = df.groupby(['JobRole', 'Attrition']).size().unstack()
jobrole_attrition.plot(kind='bar', stacked=True)
plt.title('Attrition by Job Role')
plt.xlabel('Job Role')
plt.ylabel('Count')
plt.show()
#Conclusion : The analysis reveals that attrition rates vary significantly by job role. Some job roles such as Sales Representative and Laboratory Technician have higher attrition rates compared to others indicating a strong relationship between job role and attrition.