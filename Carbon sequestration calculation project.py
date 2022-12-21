#!/usr/bin/env python
# coding: utf-8
#import Pandas, Numpy, Matplotlib.pyplot and Seaborn
# In[4]:


import pandas as pd
import numpy  as np


# In[ ]:


#Load data


# In[7]:


df =pd.read_csv("C:/Users/dell/Desktop/DATA TO CLEAN/R_DATA/ta/Tree allometry1.csv")


# In[ ]:


#View data


# In[8]:


df.head()


# In[87]:


#Check for missing observations


# In[9]:


df.isnull


# In[86]:


#Check data types


# In[10]:


df.dtypes


# In[85]:


#Change Girth to diameter for consistency in calculations to be performed 


# In[18]:


df['Diameter']=df['Girth']


# In[12]:


df.head()


# In[84]:


#Drop unwanted column


# In[27]:


df1=df.drop(['Girth'], axis=1)


# In[ ]:


#remove duplicates


# In[28]:


df1.drop_duplicates


# In[83]:


#Convert height in cm to inches


# In[29]:


df1['Height_inches']=df1['Height']*0.0328


# In[30]:


df1.head()


# In[82]:


#Square diameter


# In[33]:


df1['Dia_Squared']=df1['Diameter']*df1['Diameter']


# In[35]:


df1.head()


# In[37]:


df1.drop(['Diamter'],axis=1)


# In[81]:


#Using procedure for the calculation of CARBON (IV) OXIDE by University of Nebraska. 


# In[42]:


df1['Weight']=(df1['Dia_Squared']*0.15)*df1['Height_inches']


# In[43]:


df1['Dry_Weight']=df1['Weight']*0.725


# In[44]:


df1['Carbon_Weight']=df1['Dry_Weight']*0.5


# In[45]:


df1['C02_Weight']=df1['Carbon_Weight']*3.6663


# In[46]:


df1['C02_per_year']=df1['C02_Weight']/5


# In[47]:


df1.head()


# In[48]:


df1=df1.drop(['Diamter'],axis=1)


# In[49]:


df1.head()


# In[ ]:


#Run correlations for hypothesis (Diameter increases with Height)


# In[53]:


df_correlation = df1.corr()


# In[55]:


df_correlation.head()


# In[52]:


import matplotlib.pyplot as plt
import seaborn as  sns


# In[56]:


sns.heatmap(df_correlation, annot=True)


# In[65]:


plt.scatter(x=df1['Diameter'],y=df1['Height_inches'])
plt.title('Diameter Vs Height')
plt.xlabel('Diameter in cm')
plt.ylabel('Height in inches')
plt.show()


# In[69]:


sns.regplot(x='Diameter', y='Height_inches',data=df1, scatter_kws={'color':'red'}, line_kws={'color':'blue'})


# In[ ]:


#Plot graph showing the amount of C02 sequestered by trees


# In[80]:


sns.barplot(x='Plant ID',y='C02_per_year',data=df1)


# In[ ]:




