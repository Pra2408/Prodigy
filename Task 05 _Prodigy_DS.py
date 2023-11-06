#!/usr/bin/env python
# coding: utf-8

# In[1]:


##Import the necessary libraries:
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


##Load the dataset:
data=pd.read_excel(r"C:\Users\prachi athalye\Desktop\Accidents.xlsx")


# In[3]:


##Explore the dataset:
data.head()  
data.info()


# In[7]:


# Convert the 'Date' column to datetime format
['Date'] = pd.to_datetime(data['Date'], format='%Y-%m-%d')
# Create a new column 'Month' to extract the month from the 'Date' column
data['Month'] = data['Date'].dt.month
# Create a new column 'Weekday' to extract the weekday from the 'Date' column
data['Weekday'] = data['Date'].dt.weekday


# In[12]:


# Group the data by road conditions and calculate the number of accidents
road_conditions = data.groupby('Road_Surface_Conditions')['Accident_Index'].count().reset_index()
# Group the data by weather conditions and calculate the number of accidents
weather_conditions = data.groupby('Weather_Conditions')['Accident_Index'].count().reset_index()
# Group the data by month and calculate the number of accidents
monthly_accidents = data.groupby('Month')['Accident_Index'].count().reset_index()
# Group the data by weekday and calculate the number of accidents
weekday_accidents = data.groupby('Weekday')['Accident_Index'].count().reset_index()


# In[13]:


# Plot the number of accidents by road conditions
plt.figure(figsize=(10, 6))
sns.barplot(x='Road_Surface_Conditions', y='Accident_Index', data=road_conditions)
plt.title('Number of Accidents by Road Conditions')
plt.xlabel('Road Conditions')
plt.ylabel('Number of Accidents')
plt.show()


# In[14]:


# Plot the number of accidents by weather conditions
plt.figure(figsize=(10, 6))
sns.barplot(x='Weather_Conditions', y='Accident_Index', data=weather_conditions)
plt.title('Number of Accidents by Weather Conditions')
plt.xlabel('Weather Conditions')
plt.ylabel('Number of Accidents')
plt.show()


# In[15]:


# Plot the number of accidents by month
plt.figure(figsize=(10, 6))
sns.lineplot(x='Month', y='Accident_Index', data=monthly_accidents)
plt.title('Number of Accidents by Month')
plt.xlabel('Month')
plt.ylabel('Number of Accidents')
plt.show()


# In[16]:


# Plot the number of accidents by weekday
plt.figure(figsize=(10, 6))
sns.barplot(x='Weekday', y='Accident_Index', data=weekday_accidents)
plt.title('Number of Accidents by Weekday')
plt.xlabel('Weekday')
plt.ylabel('Number of Accidents')
plt.show()

