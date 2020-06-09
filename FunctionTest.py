# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 04:13:38 2020

@author: Mahendra
"""

def AddFunction(a,b):
    s=a+b;
    return(s)
sum=AddFunction(5,7)
print(sum)



dict={'1':'A','2':'B','3':'C','4':'D'}
if '2' in dict:
    print(dict['2'])
else:
    print('No')
    
    
    # A Python program to return multiple 
# values from a method using tuple 

# This function returns a tuple 
def fun(): 
	str = "geeksforgeeks"
	x = 20
	return str, x; # Return tuple, we could also 
					# write (str, x) 

# Driver code to test above method 
str, x = fun() # Assign returned tuple 
print(str) 
print(x) 





