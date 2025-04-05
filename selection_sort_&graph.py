def sort(num):
    for i in range(5):
        minpos=i
        for j in range(i,6):
            if num[j]<num[minpos]:
                minpos=j
        temp=num[i]
        num[i]=num[minpos]
        num[minpos]=temp
 

num=[4,18,34,3,2,1]
print(num,"number before using the selection sort ")
sort(num)
print(num,"after using the selection sort")


#### graph for selection sort::::::***********


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
plt.ylabel("time complexity for selection sort")
plt.title("graph for selection sort ")
plt.grid(True)
plt.legend()
plt.show()
