#!/usr/bin/env python
# coding: utf-8

# In[30]:


import random  #Importing random


# In[15]:


def rps(user,comp):
    if((user=='r' and comp=='s') or (user=='p' and comp=='r') or (user=='s' and comp=='p')):
        return True        
        


# In[26]:


name=input('Enter Your Name') 
upoints=0
cpoints=0
print(f'{name} VS Comp Points are {upoints}, {cpoints}')

len=int(input('Please Enter Game length'))


# In[27]:


while(len):
    len-=1
    user=input('Press r for rock,or p for paper ,or s for scissors\n').lower()
    comp=random.choice(['r','p','s'])
    if rps(user,comp):
        upoints+=1
        print('You Won')
    else:
        cpoints+=1
        print("you Lost")
    print(f'{name} VS Comp Points are {upoints}, {cpoints}')


# In[28]:


if(upoints>cpoints):
    dif=upoints-cpoints
    print(f'You won By {dif} points')
elif(upoints==cpoints):
    
    print(f'Match is a tie with { upoints} ,{cpoints}')
else:
    dif=cpoints-upoints
    print(f'You Lost By {dif} points')

