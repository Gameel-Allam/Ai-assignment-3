
# In[4]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# In[5]:

df = pd.read_csv('Wuzzuf_Jobs.csv')
df.head()

# In[6]:

df.describe()

# In[7]:

df.info()

# In[8]:

df.isnull().sum()

# In[9]:

x = df.Company.value_counts()
print(x)

# In[10]:

sorted_counts = df['Company'].value_counts()[:6]
plt.pie(sorted_counts, labels = sorted_counts.index, autopct='%1.0f%%')
plt.title("high hired company", fontsize=20)
plt.axis('square');

# In[11]:

x= df['Title'].value_counts()[:5]
x.plot(kind='barh',figsize=(15,15), color="green")

# In[12]:

x= df['Location'].value_counts()[:10]
x.plot(kind='bar',figsize=(15,10), color="green")

# In[13]:

x= df['Country'].value_counts()[:10]
x.plot(kind='bar',figsize=(15,10), color="green")