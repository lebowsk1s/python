# -*- coding: utf-8 -*-
"""
Created on Sat Nov  1 00:29:30 2014

@author: leo
"""
df = open('data.txt', 'r')
line = df.readlines()
ll = line[0].split(' ')
ll = ['f1', '02', 'f0']
sum = 0
for i in ll:
    i =  eval('0x'+i)
    sum ^= i
    #print b
print hex(sum)
