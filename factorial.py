def fac(n):
    if n<=1:
        return 1
    else:
        return n*fac(n-1)
n=5
print(f"factorial of {n} is {fac(n)}")
