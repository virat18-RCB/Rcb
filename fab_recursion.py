def fac(n):
    if n<=1:
        return n
    else:
        return fac(n-1)+fac(n-2)
for i in range(10):
    print(fac(i),end=" ")
