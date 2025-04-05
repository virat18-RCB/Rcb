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
