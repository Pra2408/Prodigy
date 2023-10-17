#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

##Load the dataset:
df = pd.read_excel(r"C:\Users\prachi athalye\Desktop\Titanic.xlsx")
##Explore the dataset:
# Display the first few rows of the dataset
print(df.head())
# Check the shape of the dataset
print(df.shape)
# Check the data types of each column
print(df.dtypes)
# Check for missing values
print(df.isnull().sum())
# Check basic statistics of numerical columns
print(df.describe())


# In[10]:


##Data Cleaning:
# Drop unnecessary columns
df = df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1)
# Fill missing values
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
# Convert categorical variables to numeric
df['Sex'] = df['Sex'].map({'female': 0, 'male': 1})
df['Embarked'] = df['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})
# Check if missing values have been filled
print(df.isnull().sum())


# In[11]:


##Exploratory Data Analysis:
# Calculate the survival rate
survival_rate = df['Survived'].mean()
print("Survival Rate:", survival_rate)
# Visualize the survival rate by gender
sns.barplot(x='Sex', y='Survived', data=df)
plt.title("Survival Rate by Gender")
plt.show()


# In[6]:


# Visualize the survival rate by passenger class
sns.barplot(x='Pclass', y='Survived', data=df)
plt.title("Survival Rate by Passenger Class")
plt.show()


# In[7]:


# Visualize the survival rate by age group
df['AgeGroup'] = pd.cut(df['Age'], bins=[0, 10, 20, 30, 40, 50, 60, 70, 80])
sns.barplot(x='AgeGroup', y='Survived', data=df)
plt.title("Survival Rate by Age Group")
plt.xticks(rotation=45)
plt.show()

