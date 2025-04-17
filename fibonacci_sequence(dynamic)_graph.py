def fib(n):
    sequence = []
    a = 0
    b = 1
    if n == 1:
        sequence.append(a)
    else:
        sequence.append(a)
        sequence.append(b)
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            sequence.append(c)
    return sequence

print("still 1", fib(1))
print("still 2", fib(2))
print("still 9", fib(9))


######################################graph>>>>>>>>>>>>>>>>>>>>>>>>>>>
import numpy as np
import matplotlib.pyplot as plt
n=np.linspace(1,50,50)
best_case=np.ones_like(n)
average_case=n
worst_case=n
plt.figure(figsize=(10,20))
plt.plot(n,best_case,label="best_case:o(n)",linewidth="2",color="red")
plt.plot(n,average_case,label="average_case:o(n)",c="blue",linewidth="2",linestyle="--")
plt.plot(n,worst_case,label="worst_case:o(n)",c="blue",linestyle=":",linewidth="2",)
plt.xlabel("input x value")
plt.ylabel("time complexity for linear search")
plt.grid(True)
plt.legend()
plt.show()
