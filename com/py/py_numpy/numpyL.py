import numpy as np
from matplotlib import pyplot as plt 
 
x = np.arange(1,11) 
y = np.sin(x) +  5 
plt.title("Matplotlib demo") 
plt.xlabel("x axis caption") 
plt.ylabel("y axis caption") 
plt.plot(x,y) 
plt.show()
a = np.array([[1,2,3],[3,4,5],[4,5,6]])  
print("*******************")
print (a[...,1])   # 第2列元素
print("*******************")
print (a[1,...])   # 第2行元素
print("*******************")
print (a[...,1:])  # 第2列及剩下的所有元素

