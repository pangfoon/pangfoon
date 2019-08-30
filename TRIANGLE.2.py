#!/usr/bin/env python
# coding: utf-8

# In[8]:


#โปรแกรมคำนวณหาความยาวด้ามสามเหลี่ยม
import math
A=float(input("A SIDE LENGTH : "))
B=float(input("B SIDE LENGTH :"))
D=float(input("CORNER C :"))
#สูตรการเปลี่ยนองศาเป็นเรเดียน
C=D*math.pi/180
#สูตรการหาค่าที่ติดราก math.sqrt
c=math.sqrt((A**2)+(B**2)-(2*A*B*math.cos(C)))
print("c = ",c, "cm.")


# In[ ]:




