#!/usr/bin/env python
# coding: utf-8

# In[7]:


import random


# In[21]:


# Lotto using Set
lotto = set()

# 6 numbers Maker

while True:
    number  = random.randrange(1, 45)
    lotto.add(number)
    if len(lotto) == 6:
        break
print(f'First 6 numbers: {lotto}')

# Bonus Maker

while True:
    bonus = random.randrange(1, 45)
    if bonus not in lotto:
        break
        
print(f'Bonus: {bonus}', end='')

