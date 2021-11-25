#!/usr/bin/env python
# coding: utf-8

# In[1]:


##This first section of the code is creating the my_BST object
##The insert and __init__ function has been taken from the tutorial content provided 

class my_BST:

    def __init__(self, value=None, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value
        self.parent = None
        
    def insert(self, value):
        if not self.value: 
            self.value = value
            return
        if self.value == value:
            return
        if value < self.value: 
            if self.left: 
                self.left.insert(value) 
                return 
            self.left = my_BST(value) 
            return 
        if self.right:
            self.right.insert(value)
            return 
        self.right =my_BST(value)
        return
##The maximum root function has been written to proceed through the tree to find the highest value
    def max(root):

        temp = root
        while temp.right is not None:
            temp = temp.right

        return temp.value
    
##The minimum root function has been written to proceed through the tree to find the lowest value

    def min(root):
        temp = root
        while temp.left is not None:
            temp = temp.left

        return temp.value
    
##The following count functions have been written to loop through the tree to identify the number of nodes
    def __count(self, root):

        if root is None:
            return 0

        if root is not None:
            return 1 + self.__count(root.left) + self.__count(root.right)

    def count(self):
        return self.__count(root=self)

    def __look(self, root, value=None):
        if root is None:
            return 0
        if root is not None:
            temp = 0
            if root.value < value:
                temp = root.value
            return temp + self.__look(root.left, value) + self.__look(root.right, value)

    def sumlower(self, value):
        root = self
        num = 0
        num += self.__look(root, value)
        return num



##The user or tester of this code must please enter their desired values of the BST within the "insert"brackets
mytree = my_BST()

mytree.insert(100)
mytree.insert(9)
mytree.insert(16)
mytree.insert(22)
mytree.insert(10)
mytree.insert(14)
mytree.insert(102)
mytree.insert(101)

##Please specify the value that would like to calculate the sum of values below it here and set is as the "thevalueof"

thevalueof=14


# In[2]:


##Part1: 
print(f'The maximum value in the tree is {mytree.max()}') 


# In[3]:


##Part 2:
print(f'The minimum value in the tree is {mytree.min()}')


# In[4]:


##Part 3:
print(f'sum of numbers in the BST that are below {thevalueof}  equals {mytree.sumlower(thevalueof)}')


# In[5]:


##Part 4:
print(f'The number of nodes in the BST are {mytree.count()}')


# In[ ]:





# In[ ]:




