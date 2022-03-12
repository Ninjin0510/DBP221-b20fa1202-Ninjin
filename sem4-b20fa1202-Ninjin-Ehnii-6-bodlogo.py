#!/usr/bin/env python
# coding: utf-8

# In[56]:


import numpy as np
a=np.arange(50,101)
print(a)


# In[57]:


b=np.zeros(10)
c=b+1
d=b+6
print(b)
print(c)
print(d)


# In[58]:


e=np.arange(20,32)
f=np.reshape(e,(3,4))
print(f)


# In[61]:


a1=np.array([1,1,1])
a2=np.diag(a1)
a3=np.array([1,2,3,4,5])
a4=np.diag(a3)
print(a2)
print(a4)


# In[60]:


b1=np.arange(4).reshape(2,2)
print(b1)
b2=b1.sum()
#Мөр
b3=b1.sum(axis=1)
print(b3)
#Багана
b4=b1.sum(axis=0)
print(b4)


# In[ ]:





# In[ ]:




