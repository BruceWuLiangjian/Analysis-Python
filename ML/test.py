# print("123")
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 20:42:24 2018

@author: 周秀珍
"""
y_replace = [1,2,1,1,1,2,2,4,3,5,6]
B_0,B_1,B_2,B_3,B_4,B_5,B_6 = [],[],[],[],[],[],[]
B0,B1,B2,B3,B4,B5,B6 = [],[],[],[],[],[],[]
for i in range(23):
     B0.append(0)

for i in range(23):
     B1.append(1)
for i in range(23):
     B2.append(2)
for i in range(23):
     B3.append(3)
for i in range(23):
     B4.append(4)
for i in range(23):
     B5.append(5)
for i in range(23):
     B6.append(6)
for index, value in enumerate(y_replace):
    if value==1:
        #for i in range(23):
            #B_1.append(1)
        y_replace=y_replace[:index+1]+B1+y_replace[index+24:]
    if value==2:
        #for i in range(23):
            #B_2.append(2)
        y_replace=y_replace[:index+1]+B2+y_replace[index+24:]
    if value==3:
        #for i in range(23):
            #B_3.append(3)
        y_replace=y_replace[:index+1]+B3+y_replace[index+24:]
    if value==4:
        #for i in range(23):
           #B_4.append(4)
        y_replace=y_replace[:index+1]+B4+y_replace[index+24:]
    if value==5:
        #for i in range(23):
            #B_5.append(5)
        y_replace=y_replace[:index+1]+B5+y_replace[index+24:]
    if value==6:
        #for i in range(23):
           #B_6.append(6)
        y_replace=y_replace[:index+1]+B6+y_replace[index+24:]
    if value==0:
        #for i in range(23):
            #B_0.append(0)
        y_replace=y_replace[:index+1]+B0+y_replace[index+24:]

print(y_replace)