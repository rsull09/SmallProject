

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("C:\python\Loan_Test.csv") #import data

df.head(10) #Read first 10 data points

df.describe() #describe numerical variables

df['Property_Area'].value_counts()

df['ApplicantIncome'].hist(bins=50)
plt.show()


df.boxplot(column='ApplicantIncome')
plt.show()


df.boxplot(column='ApplicantIncome', by='Education')
plt.show()

df['LoanAmount'].hist(bins=50)
plt.show()

df.boxplot(column='LoanAmount')
plt.show()

temp1=df['Credit_History'].value_counts(ascending=True)
temp2 = df.pivot_table(values='Loan_Status',index=['Credit_History'],aggfunc=lambda x: x.map({'Y':1,'N':0}).mean())
print "Frequency Table for Credit History"
print temp1

print'\nProbability of Getting Loan for each Credit History Class'
print temp2

import matplotlib.pyplot as plt
fig = plt.figure(figsize=(8,4))
ax1=fig.add_subplot(121)
ax1.set_xlabel('Credit_History')
ax1.set_ylabel('Count of Applicants')
ax1.set_title("Applicants by Credit_History")
temp1.plot(kind='bar')
plt.show()


df.apply(lambda x: sum(x.isnull()),axis=0)


df['LoanAmount'].fillna(df['LoanAmount'].mean(),inplace=True)


df['Self_Employed'].value_counts()


df['Self_Employed'].fillna('No',inplace=True)


table = df.pivot_table(values='LoanAmount', index='Self_Employed' ,columns='Education', aggfunc=np.median)
# Define function to return value of this pivot_table
def fage(x):
    return table.loc[x['Self_Employed'],x['Education']]
# Replace missing values
df['LoanAmount'].fillna(df[df['LoanAmount'].isnull()].apply(fage, axis=1), inplace=True)

