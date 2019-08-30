#!/usr/bin/env python
# coding: utf-8

# In[2]:


#โปรแกรมที่คำนวณหาผลรวมของจำนวนเต็มบวก
nums = [3, 5]
max = int(input("count: "))

result = 0
for i in range(0,max):
    if i%3 == 0 or i%5 == 0:
        result += i

print(result)


# In[ ]:




