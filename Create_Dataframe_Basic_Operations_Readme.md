# This below Python code executed in Jupyter Notebook [Anaconda Navidator](https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://www.anaconda.com/products/navigator&ved=2ahUKEwiT5K_m_IuNAxWce_UHHVooNSwQFnoECBkQAQ&usg=AOvVaw2FiVm4Knmhe7xplbtYwLdO) 
## We will learn to 
  1. Create a data frame using NumPy Random function
  2. Perform various logical and numerical operations

### GitHub Notebook - [Link](https://github.com/gaurav-bhatt89/Pandas/blob/main/Create_Dataframe_Basic_Operations.ipynb)
### NBViewer - [Link](https://nbviewer.org/github/gaurav-bhatt89/JupyterNotebooks/blob/main/Linear%20Regression-ECommerce_dataset-Python.ipynb)
```python
## Python - Pandas library

import numpy as np # Numerical Python library used to perform numerical operations
import pandas as pd # Pandas library used to handle and analyze structured data
from numpy.random import randn # this randn function will return sample values from a standard normal distribution

## We will create a dataframe using randn function and perform some basic operations

## pd.DataFrame - this 'DataFrame' class will help us create a DataFrame using the data 
## Since we are creating a table of 5 rows and 5 columns, we will have to specify the column and index titles
## Finally we are assigning the output of entire code to the variable 'df' which will be out dataframe
df = pd.DataFrame(randn(5,5),columns=['V','W','X','Y','Z'],index=['A','B','C','D','E'])
```
```python
## We can can check the dataframe and its some values by typing the dataframe name (We can als use .head(5) operator to limit to first 5 rows)
df
```
![image](https://github.com/user-attachments/assets/66b0965c-d618-4ecd-bc9c-b638c705464e)
```python
## To check the correlation of all the values with one another we can use the .corr function
df.corr(numeric_only=True)
```
![image](https://github.com/user-attachments/assets/216e677c-1e74-4bab-bf41-d248b01bf9df)
```python
## The .describe function will provide the general descriptive statistics of the entire dataframe 
df.describe()
```
![image](https://github.com/user-attachments/assets/32ccab9f-3e77-43e7-8d4c-acb7fd6c686a)
```python
## We can grab any columns using the bracket notation
df['W'] ## will grab only the W column

A   -0.496456
B    0.115470
C    1.345249
D    1.987287
E    0.101200
Name: W, dtype: float64

## If you want to grab two columns then
df[['W','Z']] ## add the columns names into the double brackets
```
![image](https://github.com/user-attachments/assets/9290405e-5c3a-468e-a182-cde3d2b6eee9)
```python
## If you just want the first row of column V and Z, grab it with the [0:1] after selecting the columns.
## [0:1] means that all the rows starting from index 0 to but not including index 1 (which means only row 0)
df[['V','Z']][0:1]
```
![image](https://github.com/user-attachments/assets/7157405c-9fb5-4806-9303-828b618c642f)
```pyython
## If you want to grab first two rows of columns V and Z, grab it with the [0:2] after selecting the columns.
df[['V','Z']][0:2]
```
![image](https://github.com/user-attachments/assets/39a03cd1-3de9-4117-ad70-b4b5b28c917d)
```python
## If you want to do a sum of all the rows, we can do it using the .sum operator
df.sum()

V   -1.672793
W    3.052749
X   -1.155585
Y    2.955799
Z   -3.610352
dtype: float64

## If you want to do a sum of all the columns, we can do it using the same .sum operator but this time with an axis indicator
df.sum(axis=1)

A   -3.653253
B    0.444426
C    1.174168
D    0.941053
E    0.663425
dtype: float64

## If you want to create a new column 'Total' which adds up all the values of the columns, we can do it as below
df['Total'] = df.sum(axis=1)
df
```
![image](https://github.com/user-attachments/assets/4427383a-c893-406d-a07f-3de7d77cd891)
```python
## To drop a column, use the .drop function along with the name of the column in paranthesis. Use axis=1 to specify that the 
## value to be dropped is a column, inplace=True commits the changes to the actual dataframe (it makes it permanent) 
df.drop('Total',axis=1,inplace=True)
df
```
![image](https://github.com/user-attachments/assets/6b16c99c-030b-40c6-ba12-1872512c9ec2)

# Thank You!





