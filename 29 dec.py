#!/usr/bin/env python
# coding: utf-8

# In[1]:


#lambda(this functions can take any number of arguments but can only have one expression)
addition=lambda a:a+10
print(addition(10))


# In[3]:


product=lambda a:a*8
print(product(5))


# In[4]:


divide = lambda a:a/9
print(divide(8))


# In[5]:


substraction = lambda a:a-20
print(substraction(10))


# In[6]:


#area of triangle
area = lambda h,b:h*b
print(area(5,6))


# In[7]:


#area of circle
radius=lambda r : 3.14*r
print(radius(9))


# In[8]:


#area of square
area = lambda a : a*a
print(area(8))


# In[9]:


#area of reactangle
area = lambda l,w:l*w
print(area(5,6))


# In[16]:


#filter
seq = [0,4,3,2,1,6,7]

#result of odd number
result = filter(lambda x: x % 2 !=0, seq)
print(list(result))


# In[17]:


seq = [0,5,6,3,1,5,7]
result = filter(lambda x: x % 2 == 0, seq)
print(list(result))


# In[18]:


#map
#return double of n
def addition (n):
    return n + n 
numbers = (1,2,3,4)
result = map(addition ,  numbers)
print(list(result))


# In[19]:


#reduce
import functools

lis=[4,5]
print("the max num is: ", end="")
print(functools.reduce(lambda a,b : a if a>b else b, lis))


# In[ ]:




