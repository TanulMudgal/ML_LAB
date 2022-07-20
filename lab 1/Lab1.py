#!/usr/bin/env python
# coding: utf-8

# In[47]:


import pandas as pd
import numpy as np
data=pd.read_csv('find_s.csv')
data


# In[53]:


concepts=np.array(data)[:,:-1]
concepts


# In[49]:


target=np.array(data)[:,-1]
target


# In[55]:


def train(con,tar):
    for i,val in enumerate(tar):
        if val=='yes':
            specific_h=con[i].copy()
            print(specific_h)
            break
    for i,val in enumerate(con):
        if tar[i]=='yes':
            for x in range(len(specific_h)):
                if val[x]!=specific_h[x]:
                    specific_h[x]='?'
                else:
                    pass
    return specific_h


# In[56]:


print(train(concepts,target))


# In[ ]:





# In[ ]:




