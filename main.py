# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 14:11:49 2023

@author: DanielVazquez
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("salary.csv")

df = pd.DataFrame(data)
years_np = df['YearsExperience'].to_numpy()
#print(years_np)
salary_np = df['Salary'].to_numpy()
#print(salary_np)
#x = años
#y = salario
#promedio de x
a = 0
for i in range(30):
    a = a + years_np[i]
promx = a/30
#promedio de y
b = 0
for j in range (30):
    b = b + salary_np[j]
promy = b/30

#sumatoria de (xi - xpromedio)(yi - ypromedio)
sup = 0
for h in range (30):
    sup = sup + ((years_np[h]-promx)*(salary_np[h]-promy))
#--------------------------------
#sumatoria de (xi - xpromedio)**2
inf = 0
for k in range(30):
    inf = inf + ((years_np[k] - promx)**2)
    
#valor de b1 o m
b1 = sup/inf
#valor de b0 o b = ypromedio - b1 * xpromedio
b0 = promy - (b1 * promx)
#arreglo en y prueba
arry = []
for m in range(31):
    arry.append(b0 + (m*4000))
#arreglo en x prueba 
arrx = []
for n in range(1,32):
    arrx.append(n * .4)

plt.figure()
plt.plot(years_np,salary_np,'ro')
plt.plot(arrx,arry,'b')
plt.grid()
plt.show()

