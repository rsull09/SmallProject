
# coding: utf-8

# In[20]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[8]:


df = pd.read_csv("C:\python\Loan_Test.csv") #import data


# In[9]:


df.head(10) #Read first 10 data points


# In[10]:


df.describe() #describe numerical variables


# In[11]:


df['Property_Area'].value_counts()


# In[23]:


df['ApplicantIncome'].hist(bins=50)
plt.show()


# In[22]:


df.boxplot(column='ApplicantIncome')
plt.show()


# In[26]:


df.boxplot(column='ApplicantIncome', by='Education')
plt.show()


# In[27]:


df['LoanAmount'].hist(bins=50)
plt.show()


# In[30]:


df.boxplot(column='LoanAmount')
plt.show()


# In[83]:


temp1=df['Credit_History'].value_counts(ascending=True)
temp2 = df.pivot_table(values='Loan_Status',index=['Credit_History'],aggfunc=lambda x: x.map({'Y':1,'N':0}).mean())
print "Frequency Table for Credit History"
print temp1

print'\nProbability of Getting Loan for each Credit History Class'
print temp2


# In[46]:


import matplotlib.pyplot as plt
fig = plt.figure(figsize=(8,4))
ax1=fig.add_subplot(121)
ax1.set_xlabel('Credit_History')
ax1.set_ylabel('Count of Applicants')
ax1.set_title("Applicants by Credit_History")
temp1.plot(kind='bar')
plt.show()


# In[84]:


df.apply(lambda x: sum(x.isnull()),axis=0)


# In[85]:


df['LoanAmount'].fillna(df['LoanAmount'].mean(),inplace=True)


# In[86]:


df['Self_Employed'].value_counts()


# In[87]:


df['Self_Employed'].fillna('No',inplace=True)


# In[92]:


table = df.pivot_table(values='LoanAmount', index='Self_Employed' ,columns='Education', aggfunc=np.median)
# Define function to return value of this pivot_table
def fage(x):
    return table.loc[x['Self_Employed'],x['Education']]
# Replace missing values
df['LoanAmount'].fillna(df[df['LoanAmount'].isnull()].apply(fage, axis=1), inplace=True)

