def quick_sort(num):
    if len(num)<=1:
        return num
    pt=num[0]
    left=[x for x in num[1:] if x<pt]
    right=[x for x in num[1:] if x>=pt]
    return quick_sort(left)+[pt]+quick_sort(right)
a=[43,76,2,1,9,0]
b=quick_sort(a)
print(b)


###################################graph>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

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
plt.title("the graph for quick sort")
plt.grid(True)
plt.legend()
plt.show()
