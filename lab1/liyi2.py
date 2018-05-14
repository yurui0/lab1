# -*- coding:utf-8 -*-
import csv
import numpy as np
import math

with open('iris.csv')as csvfile:
    reader=csv.reader(csvfile, delimiter=',')
    #把鸢尾花数据集的每一点的数据进行存储
    dates1 = [];dates2 = []
    #把鸢尾花数据集的每一属性的数据进行存储
    dates11=[];dates12=[];dates13=[];dates14=[]
    for row in reader:
        date1 = float(row[0]);date2 = float(row[1]);date3 = float(row[2]);date4 = float(row[3])
        dates1.append(date1);  dates1.append(date2);  dates1.append(date3);  dates1.append(date4)
        dates2.append(dates1)
        dates11.append(date1);dates12.append(date2);dates13.append(date3);dates14.append(date4)
        dates1=[]

datess2=np.array(dates2);datess11=np.array(dates11);datess12=np.array(dates12);datess13=np.array(dates13);datess14=np.array(dates14)

#归一化函数
def normal(x):
    y=x/math.sqrt((x*x).sum())
    return y

print("第一次实习第二部分第一小题")
#要对数据进行中心化和归一化
#中心化
#dates3即μ，表示每一列属性均值的数列
dates3=[]
dates3.append(datess11.mean());dates3.append(datess12.mean());dates3.append(datess13.mean());dates3.append(datess14.mean())
dates4=[]
for i in datess2:
    dates4.append(i-dates3)
datess4=np.array(dates4)
#归一化
dates5=[]
for b in datess4:
    dates5.append(normal(b))
#最后的datess5就是经过中心化和归一化之后的输入矩阵
datess5=np.array(dates5)

C=[]
D=[]
i=0
while(i<150):
    j=i
    while(j<150):
        c=np.array(datess5[i]*datess5[j])
        C.append(c.sum()*c.sum())
        j=j+1
    D.append(C)
    C=[]
    i=i+1
print("输入空间的齐次二次核矩阵")
for k in D:
    print(k)

print("第一次实习第二部分第二小题")
with open('iris.csv')as csvfile:
    reader=csv.reader(csvfile, delimiter=',')
    #把鸢尾花数据进行齐次二核化
    dates6 = [];dates7 = []
    #把每一列的结果存入不同数列进行计算
    dates20=[];dates21=[]; dates22=[];dates23=[]; dates24=[];dates25=[]; dates26=[];dates27=[]; dates28=[];dates29=[]
    for row in reader:
        date11 = float(row[0]);date12 = float(row[1]);date13 = float(row[2]);date14 = float(row[3])
        dates6.append(date11 * date11);dates6.append(date12 * date12);dates6.append(date13 * date13);dates6.append(date14 * date14)
        dates6.append(math.sqrt(2) * date11 * date12);dates6.append(math.sqrt(2) * date11 * date13);dates6.append(math.sqrt(2) * date11 * date14)
        dates6.append(math.sqrt(2) * date12 * date13);dates6.append(math.sqrt(2) * date12 * date14);dates6.append(math.sqrt(2) * date13 * date14)
        dates20.append(date11 * date11); dates21.append(date12 * date12); dates22.append(date13 * date13)
        dates23.append(date14 * date14); dates24.append(math.sqrt(2) * date11 * date12);dates25.append(math.sqrt(2) * date11 * date13)
        dates26.append(math.sqrt(2) * date11 * date14); dates27.append(math.sqrt(2) * date12 * date13)
        dates28.append(math.sqrt(2) * date12 * date14); dates29.append(math.sqrt(2) * date13 * date14)

        dates7.append(dates6)
        dates6=[]

datess7=np.array(dates7)
datess20=np.array(dates20);datess21=np.array(dates21);datess22=np.array(dates22);datess23=np.array(dates23);datess24=np.array(dates24)
datess25=np.array(dates25);datess26=np.array(dates26);datess27=np.array(dates27);datess28=np.array(dates28);datess29=np.array(dates29)
print("特征空间矩阵")
print(datess7)
#中心化
#dates8即μ，表示每一列属性均值的数列
dates8=[]
dates8.append(datess20.mean());dates8.append(datess21.mean());dates8.append(datess22.mean());dates8.append(datess23.mean())
dates8.append(datess24.mean());dates8.append(datess25.mean());dates8.append(datess26.mean());dates8.append(datess27.mean())
dates8.append(datess28.mean());dates8.append(datess29.mean())
datess8=np.array(dates8)
print(datess8)
dates9=[]
for j in datess7:
    dates9.append(j-datess8)
datess9=np.array(dates9)
#归一化
dates10=[]
for c in datess9:
    dates10.append(normal(c))
datess10=np.array(dates10)
print("经过中心化和归一化之后的结果")
print(datess10)

print("第一次实习第二部分第三小题")

E=[]
F=[]
m=0
while(m<150):
    n=m
    while(n<150):
        p=np.array(datess5[m]*datess5[n])
        E.append(p.sum()*p.sum())
        n=n+1
    F.append(E)
    E=[]
    m=m+1
print("特征空间的齐次二次核矩阵（因对称原则只显示右上的一半部分）")
for l in F:
    print(l)

print("经过比较，在输入空间通过核函数直接计算和特征空间的中心化、归一化的成对点击，结果一样")