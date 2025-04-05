def sort(num):
    for i in range(len(num)-1,0,-1):
        for j in range(i):
            if num[j]>num[j+1]:
                temp=num[j]
                num[j]=num[j+1]
                num[j+1]=temp
num=[18.17,1,7,6,2]
print(num,"before bubble sort")
sort(num)
print(num,"after bubble sort")

## graph for bubble sort::::
import matplotlib.pyplot as plt
import numpy as np
n=np.linspace(1,50,50)
best_case=n
average_case=n**2
worst_case=n**2
plt.figure(figsize=(10,20))
plt.plot(n,best_case,label="best_case:o(n)",color="green",linewidth=2)
plt.plot(n,average_case,label="average_case:o(n**2)",c="red",linewidth=2,linestyle="--")
plt.plot(n,worst_case,label="worst_case:o(n**2)",c="blue",linewidth="2",linestyle=":")
plt.xlabel("input x value")
plt.ylabel("time complexity")
plt.title("graph for bubble sort")
plt.grid(True)
plt.legend()
plt.show()
