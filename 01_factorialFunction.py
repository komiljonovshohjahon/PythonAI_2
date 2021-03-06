#!/usr/bin/env python
# coding: utf-8

# In[3]:


# factorial
def factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact *= i
    return fact


# In[4]:


num = int(input("Enter a number: "))
fact = factorial(num)
print(fact)


# In[13]:


# factorial recursion
def factorialRecursion(num):
    if num == 1:
        return 1
    return num * factorialRecursion(num-1)


# In[14]:


num = int(input("Enter a number: "))
fact = factorialRecursion(num)
print(fact)


# In[ ]:




