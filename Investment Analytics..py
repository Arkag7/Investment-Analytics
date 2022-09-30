#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importing required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[25]:


# Extracting Dataset of iNeuron From System
df=pd.read_csv(r"C:\Users\Admin\Desktop\Investment-Analytics-Ineuron-main\FDI_in_india.csv")
#Using Head Method Showing 1st 10 Data.
df.head(10)


# In[26]:


#Using Tail Method Showing 1st 10 Data.

df.tail(10)


# In[27]:


#  Sorting based on values

df.sort_values


# In[28]:


# info(), it gives information about the data set.

df.info()


# In[29]:


#Checking the names of the column

df.columns


# In[30]:


# The dataset contains 63 records and 18 different attributes / variable

df.shape


# In[31]:


# The describe() function gives the statistical summary of the numberical columns of the dataset.

df.describe()


# In[32]:


#checking null values 

df.isnull().sum()


# In[33]:


#Calculating the mean value

df.mean()


# In[35]:


#Calculating the median value 

df.median()


# In[37]:


#The mode() function is used to get the mode(s) of each element along the selected axis.

df.mode()


# In[38]:


#Checking Data Types 

df.dtypes


# In[41]:


# Maximum Investment in 2000-01 Year 

df['2000-01'].max()


# In[42]:


# Minmum Investment in 2000-01 Year 

df['2000-01'].min()


# In[44]:


# we can count the missing values in pandas series using the sum() function.

df.isna().sum()


# In[48]:


# Total Number of Sectors
df['Sector'].count()


# In[49]:


df['Sector'].value_counts()


# In[50]:


# Investment analysis for the year 2000-01 
Min_Inv=df['2000-01'].min()
Max_Inv=df['2000-01'].max()
Mean=df['2000-01'].mean()
print("Max Investment",Max_Inv)
print("Min Investment",Min_Inv)
print("Mean Investment",Mean)


# In[54]:


for i in df:
    Min_Inv=df.min()
    Max_Inv=df.max()
    Mean=df.mean()
print("Max Investment",Max_Inv)
print("Min Investment",Min_Inv)
print("Mean Investment",Mean)


# In[56]:


for i in df:
    Max_Inv=df.max()
print("Maximum Investment=",Max_Inv)


# In[57]:


Max_Inv.to_sql


# In[ ]:




