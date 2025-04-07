a=[10,20,30,40,50]
b=int(input("enter the number u have to search:"))
l=0
u=len(a)-1
while l<=u:
    mid=(l+u)//2
    if a[mid]==b:
        print("the searching element is found:",mid)
        break
    else:
        if a[mid]<b:
            l=mid+1
        else:
            u=mid-1
else:
    print("the enter value is not there in  list...")


#################graph>>>>>>>>>>>>>>>>>>>>>>>>
import numpy as np
import matplotlib.pyplot as plt
n=np.linspace(1,50,50)
best_case=np.ones_like(n)
average_case=np.log2(n)
worst_case=np.log2(n)
plt.figure(figsize=(10,20))
plt.plot(n,best_case,label="best_case:0(n)",linewidth="2",color="red")
plt.plot(n,average_case,label="average_case:o(log(n))",linewidth="2",c="yellow",linestyle="--")
plt.plot(n,worst_case,label="worst_case:o(log(n)",linewidth="2",c="blue",linestyle=':')
plt.xlabel("input x value ")
plt.ylabel("time complexity")
plt.title("graph for  binary search")
plt.grid(True)
plt.legend()
plt.show()
