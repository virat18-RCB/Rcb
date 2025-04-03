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
