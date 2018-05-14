# -*- coding:utf-8 -*-
import csv
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import stats

with open('magic04.csv')as csvfile:
    reader=csv.reader(csvfile, delimiter=',')
    #dates0-9是普通的list
    dates =[];dates1 = []; dates2 = [];dates3 = [];dates4= [];dates5 = [];dates6 = [];dates7 = [];dates8 = [];dates9 = [];dates10= []


    for row in reader:
        #第一次实习第一部分等使用
        date=float(row[0]);date1=float(row[1]);date2 = float(row[2]);date3 =float(row[3]);date4 = float(row[4])
        date5 = float(row[5]);date6 = float(row[6]);date7 = float(row[7]);date8 = float(row[8]);date9 = float(row[9])

        dates.append(date);dates1.append(date1);dates2.append(date2);dates3.append(date3);dates4.append(date4)
        dates5.append(date5);dates6.append(date6);dates7.append(date7);dates8.append(date8);dates9.append(date9)



#全是数字的数列（numpy），依次是1-10列的结果
datess=np.array(dates);datess1=np.array(dates1);datess2=np.array(dates2);datess3=np.array(dates3);datess4=np.array(dates4)
datess5=np.array(dates5);datess6=np.array(dates6);datess7=np.array(dates7);datess8=np.array(dates8);datess9=np.array(dates9)

length=len(dates)#每一列的行数

#dates10是每一列的平均数---均值
dates10.append(np.mean(datess));dates10.append(np.mean(datess1));dates10.append(np.mean(datess2));dates10.append(np.mean(datess3))
dates10.append(np.mean(datess4));dates10.append(np.mean(datess5));dates10.append(np.mean(datess6));dates10.append(np.mean(datess7))
dates10.append(np.mean(datess8));dates10.append(np.mean(datess9))

datess10=np.array(dates10)

#调用numpy的cov()计算协方差，因为一共有10对属性，因此两两配对共有45种结果
m45=np.cov(datess,datess1);m1=np.cov(datess,datess2);m2=np.cov(datess,datess3);m3=np.cov(datess,datess4);m4=np.cov(datess,datess5)
m5=np.cov(datess,datess6);m6=np.cov(datess,datess7);m7=np.cov(datess,datess8);m8=np.cov(datess,datess9);m9=np.cov(datess1,datess2)
m10=np.cov(datess1,datess3);m11=np.cov(datess1,datess4);m12=np.cov(datess1,datess5);m13=np.cov(datess1,datess6);m14=np.cov(datess1,datess7)
m15=np.cov(datess1,datess8);m16=np.cov(datess1,datess9);m17=np.cov(datess2,datess3);m18=np.cov(datess2,datess4);m19=np.cov(datess2,datess5)
m20=np.cov(datess2,datess6);m21=np.cov(datess2,datess7);m22=np.cov(datess2,datess8);m23=np.cov(datess2,datess9);m24=np.cov(datess3,datess4)
m25=np.cov(datess3,datess5);m26=np.cov(datess3,datess6);m27=np.cov(datess3,datess7);m28=np.cov(datess3,datess8);m29=np.cov(datess3,datess9)
m30=np.cov(datess4,datess5);m31=np.cov(datess4,datess6);m32=np.cov(datess4,datess7);m33=np.cov(datess4,datess8);m34=np.cov(datess4,datess9)
m35=np.cov(datess5,datess6);m36=np.cov(datess5,datess7);m37=np.cov(datess5,datess8);m38=np.cov(datess5,datess9);m39=np.cov(datess6,datess7)
m40=np.cov(datess6,datess8);m41=np.cov(datess6,datess9);m42=np.cov(datess7,datess8);m43=np.cov(datess7,datess9);m44=np.cov(datess8,datess9)

print("第一次实习第一部分第一小题")
print(datess10)

print("第一次实习第一部分第二小题")
#计算中心数据矩阵
z=datess-dates10[0];z1=datess1-dates10[1];z2=datess2-dates10[2];z3=datess3-dates10[3];z4=datess4-dates10[4]
z5=datess5-dates10[5];z6=datess6-dates10[6];z7=datess7-dates10[7];z8=datess8-dates10[8];z9=datess9-dates10[9]


Z=[];Z1=[];Z2=[];Z3=[];Z4=[];Z5=[];Z6=[];Z7=[];Z8=[];Z9=[]
#计算中心数据矩阵之间的内积，总共100个，不过对称矩阵所以只计算其中的55个
c=z*z; c1=z*z1; c2=z*z2;c3=z*z3; c4=z*z4; c5=z*z5;c6=z*z6; c7=z*z7; c8=z*z8;c9=z*z9
c10=z1*z1; c11=z1*z2;c12=z1*z3; c13=z1*z4; c14=z1*z5;c15=z1*z6; c16=z1*z7; c17=z1*z8
c18=z1*z9; c19=z2*z2; c20=z2*z3;c21=z2*z4; c22=z2*z5; c23=z2*z6;c24=z2*z7; c25=z2*z8; c26=z2*z9
c27=z3*z3; c28=z3*z4; c29=z3*z5;c30=z3*z6; c31=z3*z7; c32=z3*z8;c33=z3*z9; c34=z4*z4; c35=z4*z5
c36=z4*z6; c37=z4*z7; c38=z4*z8;c39=z4*z9; c40=z5*z5; c41=z5*z6;c42=z5*z7; c43=z5*z8; c44=z5*z9
c45=z6*z6; c46=z6*z7; c47=z6*z8;c48=z6*z9; c49=z7*z7; c50=z7*z8;c51=z7*z9; c52=z8*z8; c53=z8*z9;c54=z9*z9
#把计算得到的内积存入数组
Z.append(c.sum()/length);Z.append(c1.sum()/length);Z.append(c2.sum()/length);Z.append(c3.sum()/length);Z.append(c4.sum()/length);Z.append(c5.sum()/length);Z.append(c6.sum()/length);Z.append(c7.sum()/length);Z.append(c8.sum()/length);Z.append(c9.sum()/length)
Z1.append(c1.sum()/length);Z1.append(c10.sum()/length);Z1.append(c11.sum()/length);Z1.append(c12.sum()/length);Z1.append(c13.sum()/length);Z1.append(c14.sum()/length);Z1.append(c15.sum()/length);Z1.append(c16.sum()/length);Z1.append(c17.sum()/length);Z1.append(c18.sum()/length)
Z2.append(c2.sum()/length);Z2.append(c11.sum()/length);Z2.append(c19.sum()/length);Z2.append(c20.sum()/length);Z2.append(c21.sum()/length);Z2.append(c22.sum()/length);Z2.append(c23.sum()/length);Z2.append(c24.sum()/length);Z2.append(c25.sum()/length);Z2.append(c26.sum()/length)
Z3.append(c3.sum()/length);Z3.append(c12.sum()/length);Z3.append(c20.sum()/length);Z3.append(c27.sum()/length);Z3.append(c28.sum()/length);Z3.append(c29.sum()/length);Z3.append(c30.sum()/length);Z3.append(c31.sum()/length);Z3.append(c32.sum()/length);Z3.append(c33.sum()/length)
Z4.append(c4.sum()/length);Z4.append(c13.sum()/length);Z4.append(c21.sum()/length);Z4.append(c28.sum()/length);Z4.append(c34.sum()/length);Z4.append(c35.sum()/length);Z4.append(c36.sum()/length);Z4.append(c37.sum()/length);Z4.append(c38.sum()/length);Z4.append(c39.sum()/length)
Z5.append(c5.sum()/length);Z5.append(c14.sum()/length);Z5.append(c22.sum()/length);Z5.append(c29.sum()/length);Z5.append(c35.sum()/length);Z5.append(c40.sum()/length);Z5.append(c41.sum()/length);Z5.append(c42.sum()/length);Z5.append(c43.sum()/length);Z5.append(c44.sum()/length)
Z6.append(c6.sum()/length);Z6.append(c15.sum()/length);Z6.append(c23.sum()/length);Z6.append(c30.sum()/length);Z6.append(c36.sum()/length);Z6.append(c41.sum()/length);Z6.append(c45.sum()/length);Z6.append(c46.sum()/length);Z6.append(c47.sum()/length);Z6.append(c48.sum()/length)
Z7.append(c7.sum()/length);Z7.append(c16.sum()/length);Z7.append(c24.sum()/length);Z7.append(c31.sum()/length);Z7.append(c37.sum()/length);Z7.append(c42.sum()/length);Z7.append(c46.sum()/length);Z7.append(c49.sum()/length);Z7.append(c50.sum()/length);Z7.append(c51.sum()/length)
Z8.append(c8.sum()/length);Z8.append(c17.sum()/length);Z8.append(c25.sum()/length);Z8.append(c32.sum()/length);Z8.append(c38.sum()/length);Z8.append(c43.sum()/length);Z8.append(c47.sum()/length);Z8.append(c50.sum()/length);Z8.append(c52.sum()/length);Z8.append(c53.sum()/length)
Z9.append(c9.sum()/length);Z9.append(c18.sum()/length);Z9.append(c26.sum()/length);Z9.append(c33.sum()/length);Z9.append(c39.sum()/length);Z9.append(c44.sum()/length);Z9.append(c48.sum()/length);Z9.append(c51.sum()/length);Z9.append(c53.sum()/length);Z9.append(c54.sum()/length)

print(Z);print(Z1);print(Z2);print(Z3);print(Z4);print(Z5);print(Z6);print(Z7);print(Z8);print(Z9)


print("第一次实习第一部分第三小题")
#声明数列存储数据
f=[];f1=[];f2=[];f3=[];f4=[];f5=[];f6=[];f7=[];f8=[];f9=[]
f10=[];f11=[];f12=[];f13=[];f14=[];f15=[];f16=[];f17=[];f18=[];f19=[]
f20=[];f21=[];f22=[];f23=[];f24=[];f25=[];f26=[];f27=[];f28=[];f29=[]
f30=[];f31=[];f32=[];f33=[];f34=[];f35=[];f36=[];f37=[];f38=[];f39=[]
f40=[];f41=[];f42=[];f43=[];f44=[];f45=[];f46=[];f47=[];f48=[];f49=[]
f50=[];f51=[];f52=[];f53=[];f54=[];f55=[];f56=[];f57=[];f58=[];f59=[]
f60=[];f61=[];f62=[];f63=[];f64=[];f65=[];f66=[];f67=[];f68=[];f69=[]
f70=[];f71=[];f72=[];f73=[];f74=[];f75=[];f76=[];f77=[];f78=[];f79=[]
f80=[];f81=[];f82=[];f83=[];f84=[];f85=[];f86=[];f87=[];f88=[];f89=[]
f90=[];f91=[];f92=[];f93=[];f94=[];f95=[];f96=[];f97=[];f98=[];f99=[]

#计算具体的每一个单独的外积zi*zj，并进行保存
i=0
while(i<length):
    e = z[i] * z[i]; e1 = z[i] * z1[i]; e2 = z[i] * z2[i]; e3 = z[i] * z3[i]; e4 = z[i] * z4[i]; e5 = z[i] * z5[i]
    e6 = z[i] * z6[i];e7 = z[i] * z7[i];e8 = z[i] * z8[i];e9 = z[i] * z9[i];e10 = z1[i] * z1[i]; e11 = z1[i] * z2[i]
    e12 = z1[i] * z3[i];e13 = z1[i] * z4[i]; e14 = z1[i] * z5[i]; e15 = z1[i] * z6[i]; e16 = z1[i] * z7[i]; e17 = z1[i] * z8[i]
    e18 = z1[i] * z9[i]; e19 = z2[i] * z2[i]; e20 = z2[i] * z3[i]; e21 = z2[i] * z4[i]; e22 = z2[i] * z5[i]; e23= z2[i] * z6[i]
    e24 = z2[i] * z7[i]; e25 = z2[i] * z8[i]; e26 = z2[i] * z9[i]; e27 = z3[i] * z3[i]; e28 = z3[i] * z4[i]; e29 = z3[i] * z5[i]
    e30 = z3[i] * z6[i]; e31 = z3[i] * z7[i]; e32 = z3[i] * z8[i]; e33 = z3[i] * z9[i]; e34 = z4[i] * z4[i]; e35 = z4[i] * z5[i]
    e36 = z4[i] * z6[i]; e37 = z4[i] * z7[i]; e38 = z4[i] * z8[i]; e39 = z4[i] * z9[i]; e40 = z5[i] * z5[i]; e41 = z5[i] * z6[i]
    e42 = z5[i] * z7[i]; e43 = z5[i] * z8[i]; e44 = z5[i] * z9[i]; e45 = z6[i] * z6[i]; e46 = z6[i] * z7[i]; e47 = z6[i] * z8[i]
    e48 = z6[i] * z9[i]; e49 = z7[i] * z7[i]; e50 = z7[i] * z8[i]; e51 = z7[i] * z9[i]; e52 = z8[i] * z8[i]; e53 = z8[i] * z9[i];e54 = z9[i] * z9[i]

    f.append(e); f1.append(e1); f2.append(e2); f3.append(e3); f4.append(e4); f5.append(e5); f6.append(e6); f7.append(e7); f8.append(e8); f9.append(e9)
    f10.append(e1); f11.append(e10); f12.append(e11); f13.append(e12); f14.append(e13); f15.append(e14); f16.append(e15); f17.append(e16); f18.append(e17); f19.append(e18)
    f20.append(e2); f21.append(e11); f22.append(e19); f23.append(e20); f24.append(e21); f25.append(e22); f26.append(e23); f27.append(e24); f28.append(e25); f29.append(e26)
    f30.append(e3); f31.append(e12); f32.append(e20); f33.append(e27); f34.append(e28); f35.append(e29); f36.append(e30); f37.append(e31); f38.append(e32); f39.append(e33)
    f40.append(e4); f41.append(e13); f42.append(e21); f43.append(e28); f44.append(e34); f45.append(e35); f46.append(e36); f47.append(e37); f48.append(e38); f49.append(e39)
    f50.append(e5); f51.append(e14); f52.append(e22); f53.append(e29); f54.append(e35); f55.append(e40); f56.append(e41); f57.append(e42); f58.append(e43); f59.append(e44)
    f60.append(e6); f61.append(e15); f62.append(e23); f63.append(e30); f64.append(e36); f65.append(e41); f66.append(e45); f67.append(e46); f68.append(e47); f69.append(e48)
    f70.append(e7); f71.append(e16); f72.append(e24); f73.append(e31); f74.append(e37); f75.append(e42); f76.append(e46); f77.append(e49); f78.append(e50); f79.append(e51)
    f80.append(e8); f81.append(e17); f82.append(e25); f83.append(e32); f84.append(e38); f85.append(e43); f86.append(e47); f87.append(e50); f88.append(e52); f89.append(e53)
    f90.append(e9); f91.append(e18); f92.append(e26); f93.append(e33); f94.append(e39); f95.append(e44); f96.append(e48); f97.append(e51); f98.append(e53); f99.append(e54)

    i=i+1

ff=np.array(f);ff1=np.array(f1);ff2=np.array(f2);ff3=np.array(f3);ff4=np.array(f4);ff5=np.array(f5);ff6=np.array(f6);ff7=np.array(f7);ff8=np.array(f8);ff9=np.array(f9)
ff10=np.array(f10);ff11=np.array(f11);ff12=np.array(f12);ff13=np.array(f13);ff14=np.array(f14);ff15=np.array(f15);ff16=np.array(f16);ff17=np.array(f17);ff18=np.array(f18);ff19=np.array(f19)
ff20=np.array(f20);ff21=np.array(f21);ff22=np.array(f22);ff23=np.array(f23);ff24=np.array(f24);ff25=np.array(f25);ff26=np.array(f26);ff27=np.array(f27);ff28=np.array(f28);ff29=np.array(f29)
ff30=np.array(f30);ff31=np.array(f31);ff32=np.array(f32);ff33=np.array(f33);ff34=np.array(f34);ff35=np.array(f35);ff36=np.array(f36);ff37=np.array(f37);ff38=np.array(f38);ff39=np.array(f39)
ff40=np.array(f40);ff41=np.array(f41);ff42=np.array(f42);ff43=np.array(f43);ff44=np.array(f44);ff45=np.array(f45);ff46=np.array(f46);ff47=np.array(f47);ff48=np.array(f48);ff49=np.array(f49)
ff50=np.array(f50);ff51=np.array(f51);ff52=np.array(f52);ff53=np.array(f53);ff54=np.array(f54);ff55=np.array(f55);ff56=np.array(f56);ff57=np.array(f57);ff58=np.array(f58);ff59=np.array(f59)
ff60=np.array(f60);ff61=np.array(f61);ff62=np.array(f62);ff63=np.array(f63);ff64=np.array(f64);ff65=np.array(f65);ff66=np.array(f66);ff67=np.array(f67);ff68=np.array(f68);ff69=np.array(f69)
ff70=np.array(f70);ff71=np.array(f71);ff72=np.array(f72);ff73=np.array(f73);ff74=np.array(f74);ff75=np.array(f75);ff76=np.array(f76);ff77=np.array(f77);ff78=np.array(f78);ff79=np.array(f79)
ff80=np.array(f80);ff81=np.array(f81);ff82=np.array(f82);ff83=np.array(f83);ff84=np.array(f84);ff85=np.array(f85);ff86=np.array(f86);ff87=np.array(f87);ff88=np.array(f88);ff89=np.array(f89)
ff90=np.array(f90);ff91=np.array(f91);ff92=np.array(f92);ff93=np.array(f93);ff94=np.array(f94);ff95=np.array(f95);ff96=np.array(f96);ff97=np.array(f97);ff98=np.array(f98);ff99=np.array(f99)

g=[];g1=[];g2=[];g3=[];g4=[];g5=[];g6=[];g7=[];g8=[];g9=[]
#通过求和计算总的外积
g.append(ff.sum()/length);g.append(ff10.sum()/length);g.append(ff20.sum()/length);g.append(ff30.sum()/length);g.append(ff40.sum()/length)
g1.append(ff1.sum()/length);g1.append(ff11.sum()/length);g1.append(ff21.sum()/length);g1.append(ff31.sum()/length);g1.append(ff41.sum()/length)
g1.append(ff51.sum()/length);g1.append(ff61.sum()/length);g1.append(ff71.sum()/length);g1.append(ff81.sum()/length);g1.append(ff91.sum()/length)
g2.append(ff2.sum()/length);g2.append(ff12.sum()/length);g2.append(ff22.sum()/length);g2.append(ff32.sum()/length);g2.append(ff42.sum()/length)
g2.append(ff52.sum()/length);g2.append(ff62.sum()/length);g2.append(ff72.sum()/length);g2.append(ff82.sum()/length);g2.append(ff92.sum()/length)
g3.append(ff3.sum()/length);g3.append(ff13.sum()/length);g3.append(ff23.sum()/length);g3.append(ff33.sum()/length);g3.append(ff43.sum()/length)
g3.append(ff53.sum()/length);g3.append(ff63.sum()/length);g3.append(ff73.sum()/length);g3.append(ff83.sum()/length);g3.append(ff93.sum()/length)
g4.append(ff4.sum()/length);g4.append(ff14.sum()/length);g4.append(ff24.sum()/length);g4.append(ff34.sum()/length);g4.append(ff44.sum()/length)
g4.append(ff54.sum()/length);g4.append(ff64.sum()/length);g4.append(ff74.sum()/length);g4.append(ff84.sum()/length);g4.append(ff94.sum()/length)
g5.append(ff5.sum()/length);g5.append(ff15.sum()/length);g5.append(ff25.sum()/length);g5.append(ff35.sum()/length);g5.append(ff45.sum()/length)
g5.append(ff55.sum()/length);g5.append(ff65.sum()/length);g5.append(ff75.sum()/length);g5.append(ff85.sum()/length);g5.append(ff95.sum()/length)
g6.append(ff6.sum()/length);g6.append(ff16.sum()/length);g6.append(ff26.sum()/length);g6.append(ff36.sum()/length);g6.append(ff46.sum()/length)
g6.append(ff56.sum()/length);g6.append(ff66.sum()/length);g6.append(ff76.sum()/length);g6.append(ff86.sum()/length);g6.append(ff96.sum()/length)
g7.append(ff7.sum()/length);g7.append(ff17.sum()/length);g7.append(ff27.sum()/length);g7.append(ff37.sum()/length);g7.append(ff47.sum()/length)
g7.append(ff57.sum()/length);g7.append(ff67.sum()/length);g7.append(ff77.sum()/length);g7.append(ff87.sum()/length);g7.append(ff97.sum()/length)
g8.append(ff8.sum()/length);g8.append(ff18.sum()/length);g8.append(ff28.sum()/length);g8.append(ff38.sum()/length);g8.append(ff48.sum()/length)
g8.append(ff58.sum()/length);g8.append(ff68.sum()/length);g8.append(ff78.sum()/length);g8.append(ff88.sum()/length);g8.append(ff98.sum()/length)
g9.append(ff9.sum()/length);g9.append(ff19.sum()/length);g9.append(ff29.sum()/length);g9.append(ff39.sum()/length);g9.append(ff49.sum()/length)
g9.append(ff59.sum()/length);g9.append(ff69.sum()/length);g9.append(ff79.sum()/length);g9.append(ff89.sum()/length);g9.append(ff99.sum()/length)

print(g);print(g1);print(g2);print(g3);print(g4);print(g5);print(g6);print(g7);print(g8);print(g9)



print("第一次实习第一部分第四小题")
#计算两个向量的积
d=(z*z1).sum()
#计算算两个向量的模
d1=math.sqrt((z*z).sum());d2=math.sqrt((z1*z1).sum())
d3=d/(d1*d2)
print("第一属性与第二属性的夹角cos为")
print(d3)
#绘制点集的函数
plt.scatter(datess,datess1)
plt.show()


print("第一次实习第一部分第五小题")
#计算E[X1^2]
m=(datess*datess).sum()/float(length)
#计算E[X1]*E[X1]
n=datess10[0]*datess10[0]
#根据公式： 方差=E[X1^2]-E[X1]*E[X1]来计算
sigma=math.sqrt(m-n)
#计算属性一的均值
mu=datess10[0]

x=datess
x.sort()
x1=np.arange(-110,250,1)
#调用pdf的正太分布函数显示图像
y=stats.norm.pdf(x1,mu,sigma)
plt.plot(x1,y)
plt.show()


print("第一次实习第一部分第六小题")
print("依次输出各个属性的方差")
#调用numpy库的var函数计算属性的方差
print(datess.var());print(datess1.var());print(datess2.var());print(datess3.var())
print(datess4.var());print(datess5.var());print(datess6.var());print(datess7.var())
print(datess8.var());print(datess9.var())



print("第一次实习第一部分第七小题")
print("属性1-2的协方差");print(m45[0][1]);print("属性1-3的协方差");print(m1[0][1]);print("属性1-4的协方差");print(m2[0][1]);print("属性1-5的协方差");print(m3[0][1]);print("属性1-6的协方差");print(m4[0][1])
print("属性1-7的协方差");print(m5[0][1]);print("属性1-8的协方差");print(m6[0][1]);print("属性1-9的协方差");print(m7[0][1]);print("属性1-10的协方差");print(m8[0][1]);print("属性2-3的协方差");print(m9[0][1])
print("属性2-4的协方差");print(m10[0][1]);print("属性2-5的协方差");print(m11[0][1]);print("属性2-6的协方差");print(m12[0][1]);print("属性2-7的协方差");print(m13[0][1]);print("属性2-8的协方差");print(m14[0][1])
print("属性2-9的协方差");print(m15[0][1]);print("属性2-10的协方差");print(m16[0][1]);print("属性3-4的协方差");print(m17[0][1]);print("属性3-5的协方差");print(m18[0][1]);print("属性3-6的协方差");print(m19[0][1])
print("属性3-7的协方差");print(m20[0][1]);print("属性3-8的协方差");print(m21[0][1]);print("属性3-9的协方差");print(m22[0][1]);print("属性3-10的协方差");print(m23[0][1]);print("属性4-5的协方差");print(m24[0][1])
print("属性4-6的协方差");print(m25[0][1]);print("属性4-7的协方差");print(m26[0][1]);print("属性4-8的协方差");print(m27[0][1]);print("属性4-9的协方差");print(m28[0][1]);print("属性4-10的协方差");print(m29[0][1])
print("属性5-6的协方差");print(m30[0][1]);print("属性5-7的协方差");print(m31[0][1]);print("属性5-8的协方差");print(m32[0][1]);print("属性5-9的协方差");print(m33[0][1]);print("属性5-10的协方差");print(m34[0][1])
print("属性6-7的协方差");print(m35[0][1]);print("属性6-8的协方差");print(m36[0][1]);print("属性6-9的协方差");print(m37[0][1]);print("属性6-10的协方差");print(m38[0][1]);print("属性7-8的协方差");print(m39[0][1])
print("属性7-9的协方差");print(m40[0][1]);print("属性7-10的协方差");print(m41[0][1]);print("属性8-9的协方差");print(m42[0][1]);print("属性8-10的协方差");print(m43[0][1]);print("属性9-10的协方差");print(m44[0][1])

