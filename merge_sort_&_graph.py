def merge_sort(num):
    if len(num)>1:
        mid=(len(num))//2
        left=num[:mid]
        right=num[mid:]
        merge_sort(left)
        merge_sort(right)
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                num[k]=left[i]
                i+=1
            else:
                num[k]=right[j]
                j+=1
            k+=1
        while i<len(left):
            num[k]=left[i]
            i+=1
            j+=1
        while j<len(right):
            num[k]=right[j]
            j+=1
            k+=1
a=[43,5,1,3,78,6]
merge_sort(a)
print(a)


############################################graph*********************************

import numpy as np
import matplotlib.pyplot as plt
n=np.linspace(1,50,50)
best_case=n*np.log2(n)
average_case=n*np.log2(n)
worst_case=n*np.log2(n)
plt.figure(figsize=(10,20))
plt.plot(n,best_case,label="best_case:0(n(log(n)))",linewidth="2",color="red")
plt.plot(n,average_case,label="average_case:o(n(log(n)))",linewidth="2",c="blue",linestyle="--")
plt.plot(n,worst_case,label="worst_case:o(n(log(n)))",linewidth="2",c="blue",linestyle=":")
plt.xlabel("input (x)")
plt.ylabel("time complexity")
plt.title("the graph for merge sort")
plt.grid(True)
plt.legend()
plt.show()
