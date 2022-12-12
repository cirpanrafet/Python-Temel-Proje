#!/usr/bin/env python
# coding: utf-8

# In[12]:


#SORU 1
a = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
b = []

def flatten(n):
    for i in n :
        if isinstance(i,list):
            flatten(i)
        else:
            b.append(i)


flatten(a)
print(b)



# In[13]:


#SORU 2
a = [[1, 2], [3, 4], [5, 6, 7]]
a.reverse()http://localhost:8888/notebooks/Untitled1.ipynb?kernel_name=python3#
for i in range(len(a)):
    (a[i])=(a[i])[::-1]
print(a)


# In[ ]:




