#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 27 16:35:02 2020

@author: szilard
"""


class NUMBER():
    def __init__(self,num):
            self.num=num
    
    def get_number(self): 
        return self.num
        
    def IsItInteger(self):
        try: 
            self.num=int(self.num)
            return True
        except: return False
        
    def IsItEven(self):
        if not(self.num%2) : return True
        else: return False
    
    def CountDigits(self):
        digits=1
        checkbit=False
        i=10
        while not(checkbit):
            if (self.num/i)>=1:
                digits+=1
                i*=10
            else : checkbit=True
            
        return digits



# print(str(number.IsItInteger()))
# print(str(number.CountDigits()))
# print(str(number.IsItEven()))
            
