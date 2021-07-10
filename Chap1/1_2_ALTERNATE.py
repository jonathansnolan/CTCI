# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 20:39:57 2021

@author: Emily
"""

def permuatation(str1, str2):
    if len(str1) != len(str2):
        return False
    
    str1 = sorted(str1)
    str2 = sorted(str2)
    
    for k in range(len(str1)):
        if str1[k] != str2[k]:
            return False
        
    return True
    
print(permuatation("amy", "may"))