#!/usr/bin/env python
# coding: utf-8

# In[3]:


a = float(input("enter the first number"))
b = float(input("enter the second number"))
c = float(input("enter the third number"))
if a>b and a>c:
    print(a, "is the largest")
elif b>c:
    print(b, "is the largest")
else:
    print(c, "is the largest")


# In[ ]:


std_list = ["Amit","Rahul", "Priya", "Sneha"]
print("\n Student List \n", std_list)

std_tuple = ["Amit","Rahul", "Priya", "Sneha"]
print("\n Student Tuple \n", std_tuple)


# In[ ]:


user ={1: "Amit",
       2: "Jane",
       3: "Rohit",
       4: "Sneha",
       5: "Shreya"}
del user[2]
print(user)

