# This below Python code executed in Jupyter Notebook by [Anaconda Navigator](https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://www.anaconda.com/products/navigator&ved=2ahUKEwiT5K_m_IuNAxWce_UHHVooNSwQFnoECBkQAQ&usg=AOvVaw2FiVm4Knmhe7xplbtYwLdO) 
## We will learn to 
  1. Create a data frame using [NumPy](https://numpy.org/) Random function
  2. Perform various logical and numerical operations (Part-2)

### GitHub Notebook - [Link](https://github.com/gaurav-bhatt89/Pandas/blob/main/Create_Dataframe_Basic_Operations-Part%202.ipynb)
### NBViewer - [Link](https://nbviewer.org/github/gaurav-bhatt89/Pandas/blob/main/Create_Dataframe_Basic_Operations-Part%202.ipynb)
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
![image](https://github.com/user-attachments/assets/70bdbfc6-8aa7-494f-9881-955b9962884b)
### Conditional Operators
```python
df > 0
```
![image](https://github.com/user-attachments/assets/3fc53d44-8e34-4d7b-865a-753538ace505)
```python
## Lets pass this conditional operator and return a dataframe with Non-Null values
df[df>0]
```
![image](https://github.com/user-attachments/assets/b5c3e534-9ef7-4542-beff-0aa71a08b80e)
```python

## We can also pass this non zero condition over an individual colums
df['W']>0

A    False
B     True
C     True
D     True
E     True
Name: W, dtype: bool
```
```python
## By passing a conditional statement inside a dataframe will return all non zero values inside a new dataframe
df[df['W']>0]
```
![image](https://github.com/user-attachments/assets/c63d2fff-ea9f-4d51-a52f-e839b91085f0)
```python
## Lets say we want to use multiple conditions to filter out the data
## We will filter it out by all those rows in column Z where the value is < 0 and all those rows in columns W where the value is > 0
df[(df['Z']<0)&(df['W']>0)]
```
![image](https://github.com/user-attachments/assets/1ba62e8c-bb65-4d7e-b43d-b7ec38605838)
```python
## From the obtained results, we can further filter it out depending on which row we want. Lets say we only want row B
df[(df['Z']<0)&(df['W']>0)].loc['B']

V   -1.817734
W    1.514598
X   -1.095995
Y    1.599770
Z   -0.664676
Name: B, dtype: float64
```
```python
## Lets change the index from A...E to some random States of India
## Lets create states as a list, split it indvidually and add it as a new column to existing dataframe
states = 'MH GJ UK KA RJ'.split()
df['States'] = states
df
```
![image](https://github.com/user-attachments/assets/5749a19d-6d9a-4b33-a887-213a6ac19c76)
```python
df.set_index(df['States'],inplace=True) ## We are setting the index to states
df.drop('States',axis=1,inplace=True) # No longer we now need to States column so dropping entire column
df
```
![image](https://github.com/user-attachments/assets/e6e17455-cbf3-4c91-ad27-dfd7ea69c98f)

## Thank You




