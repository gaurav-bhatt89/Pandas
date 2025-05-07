#!/usr/bin/env python
# coding: utf-8

# In[3]:


## Python - Pandas library 


# In[4]:


import numpy as np # Numerical Python library used to perform numerical operations
import pandas as pd # Pandas library used to handle and analyze structured data


# In[5]:


from numpy.random import randn # this randn function will return sample values from a standard normal distribution


# In[6]:


## We will create a dataframe using randn function and perform some basic operations


# In[7]:


## pd.DataFrame - this 'DataFrame' class will help us create a DataFrame using the data 
## Since we are creating a table of 5 rows and 5 columns, we will have to specify the column and index titles
## Finally we are assigning the output of entire code to the variable 'df' which will be out dataframe
df = pd.DataFrame(randn(5,5),columns=['V','W','X','Y','Z'],index=['A','B','C','D','E'])


# In[8]:


## We can can check the dataframe and its some values by typing the dataframe name (We can als use .head(5) operator to limit to first 5 rows)
df


# ### Conditional Operators

# In[28]:


df > 0


# In[30]:


## Lets pass this conditional operator and return a dataframe with Non-Null values
df[df>0]


# In[35]:


## We can also pass this non zero condition over an individual colums
df['W']>0


# In[39]:


## By passing a conditional statement inside a dataframe will return all non zero values inside a new dataframe
df[df['W']>0]


# In[51]:


## Lets say we want to use multiple conditions to filter out the data
## We will filter it out by all those rows in column Z where the value is < 0 and all those rows in columns W where the value is > 0
df[(df['Z']<0)&(df['W']>0)]


# In[85]:


## From the obtained results, we can further filter it out depending on which row we want. Lets say we only want row B
df[(df['Z']<0)&(df['W']>0)].loc['B']


# In[87]:


df


# In[ ]:


## Lets change the index from A...E to some random States of India


# In[104]:


## Lets create states as a list, split it indvidually and add it as a new column to existing dataframe
states = 'MH GJ UK KA RJ'.split()
df['States'] = states
df


# In[119]:


df.set_index(df['States'],inplace=True) ## We are setting the index to states
df.drop('States',axis=1,inplace=True) # No longer we now need to States column so dropping entire column
df


# ## Thank You
