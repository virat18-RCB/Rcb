def sort(num):
    for i in range(1,len(num)):
        j=i
        while num[j-1]>num[j] and j>0:
            num[j-1],num[j]=num[j],num[j-1]
            j-=1
num=[21,3,1,4,6,18]
print(num,"before using a insertion sort")
sort(num)
print(num,"after using a insertion sort")


 #####graph for insertion sort**************

import matplotlib.pyplot as plt
import numpy as np
n=np.linspace(1,50,50)
best_case=n**2
average_case=n**2
worst_case=n**2
plt.figure(figsize=(10,20))
plt.plot(n,best_case,label="best_case:0(n**2)",color="red",linewidth="2")
plt.plot(n,average_case,label="average_case:0(n**2)",c="green",linewidth='2',linestyle='-')
plt.plot(n,worst_case,label="worst_case:o(n**2)",c="blue",linewidth='2',linestyle=":")
plt.xlabel("input x value ")
plt.ylabel("time complexity for insertion sort")
plt.title("graph for insertion  sort ")
plt.grid(True)
plt.legend()
plt.show()
