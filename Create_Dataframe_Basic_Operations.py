#!/usr/bin/env python
# coding: utf-8

# In[1]:


## Python - Pandas library 


# In[7]:


import numpy as np # Numerical Python library used to perform numerical operations
import pandas as pd # Pandas library used to handle and analyze structured data


# In[14]:


from numpy.random import randn # this randn function will return sample values from a standard normal distribution


# In[16]:


## We will create a dataframe using randn function and perform some basic operations


# In[20]:


## pd.DataFrame - this 'DataFrame' class will help us create a DataFrame using the data 
## Since we are creating a table of 5 rows and 5 columns, we will have to specify the column and index titles
## Finally we are assigning the output of entire code to the variable 'df' which will be out dataframe
df = pd.DataFrame(randn(5,5),columns=['V','W','X','Y','Z'],index=['A','B','C','D','E'])


# In[26]:


## We can can check the dataframe and its some values by typing the dataframe name (We can als use .head(5) operator to limit to first 5 rows)
df


# In[70]:


## To check the correlation of all the values with one another we can use the .corr function
df.corr(numeric_only=True)


# In[72]:


## The .describe function will provide the general descriptive statistics of the entire dataframe 
df.describe()


# In[30]:


## We can grab any columns using the bracket notation
df['W'] ## will grab only the W column


# In[34]:


## If you want to grab two columns then
df[['W','Z']] ## add the columns names into the double brackets


# In[44]:


## If you just want the first row of column V and Z, grab it with the [0:1] after selecting the columns.
## [0:1] means that all the rows starting from index 0 to but not including index 1 (which means only row 0)
df[['V','Z']][0:1]


# In[46]:


## If you want to grab first two rows of columns V and Z, grab it with the [0:2] after selecting the columns.
df[['V','Z']][0:2]


# In[54]:


## If you want to do a sum of all the rows, we can do it using the .sum operator
df.sum()


# In[56]:


## If you want to do a sum of all the columns, we can do it using the same .sum operator but this time with an axis indicator
df.sum(axis=1)


# In[68]:


## If you want to create a new column 'Total' which adds up all the values of the columns, we can do it as below
df['Total'] = df.sum(axis=1)
df


# In[74]:


## To drop a column, use the .drop function along with the name of the column in paranthesis. Use axis=1 to specify that the 
## value to be dropped is a column, inplace=True commits the changes to the actual dataframe (it makes it permanent) 
df.drop('Total',axis=1,inplace=True)
df


# ## Thank You
