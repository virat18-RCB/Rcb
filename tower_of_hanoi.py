def hanoi(n,s,a,d):
    if n>0:
        hanoi(n-1,s,d,a)
        print(f"moves {n} from {s} to {d}")
        hanoi(n-1,a,s,d)
hanoi(3,"a","b","c")
