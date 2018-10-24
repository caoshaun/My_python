# -*- coding: utf-8 -*-

import math
import numpy
#实验一：测量量的不确定度计算

#输入数据
print("数据录入")
#cylinder_h=['0.694','0.698','0.7','0.695','0.705','0.702']
cylinder_h=[]
num=float(input("每个物理量测量几次？\n"))
i=0
while i<num:
    a=input("请输入单次的数值，并回车：\n")
    cylinder_h.append(a)
    i+=1
print(cylinder_h)

#计算平均值
all=0
for b in cylinder_h:
    all = float(b)+all
average=float(all/num)
print("平均值为：", average)

#A类计算不确定度
i = 0
sum_muA = 0
while i < num:
    for c in cylinder_h:
        sum_muA = (float(c)-average) ** (2) +sum_muA
        i += 1
muA = (sum_muA/(num*(num-1)))**(1/2)
print("第一类不确定度：", muA)

#计算不确定度
accuracy = float(input("请输入精确度\n"))
#print('本次运算，仪器不确定度计算时除以3^(1/2)，置信率为95%')
muB=accuracy/(3)**(1/2)
muC=((muA)**(2)+(muB)**(2))**(1/2)
Ex=(muC*2)/average
print('muB:', muB)
print("不确定度：", muC, "Ex:", Ex)
print("最终的答案：", average, "+-", 2*muC)

