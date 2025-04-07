a=[10,20,30,40]
b=int(input('enter the number'))
for i in range(len(a)):
    if a[i]==b:
        print("THE VALUE IS FOUND",i)
        break
else:
    print("the number not found:")


###############graph for linear search##################

import numpy as np
import matplotlib.pyplot as plt
n=np.linspace(1,50,50)
best_case=np.ones_like(n)
average_case=n
worst_case=n
plt.figure(figsize=(10,20))
plt.plot(n,best_case,label="best_case:0(1)",linewidth="2",color="red")
plt.plot(n,average_case,label="average_case:o(n)",c="blue",linewidth="2",linestyle="--")
plt.plot(n,worst_case,label="worst_case:o(n)",c="blue",linestyle=":",linewidth="2",)
plt.xlabel("input x value")
plt.ylabel("time complexity for linear search")
plt.grid(True)
plt.legend()
plt.show()
