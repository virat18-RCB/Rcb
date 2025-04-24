###list####
l=[]
print("the list is empty",l)
l=[10,20,30]
print("the number are field in the list ",l)
l=[1,3,"aa",4,5]
print("the mixed value in the list",l)
l=["q","w","e"]
print("the string",l)
print(l[0])
print(l[0:2])
l=[["q","W"],["a","b"]]
print(l)

#####dictonary#####
a={}
print("empty list",a)
a=dict({1:"mon",2:"tue"})
print(a)
a=dict([(1,"mon"),(2,"tur")])
print(a)

###################tuple##############
t=(0,)
print("single tuple",t)
t=(1,2,3,4)
print("multiple tuple",t)
t=0,1,2,3,4
print("without parameter",t)
t=("abc",("ada","baa"))
print(" nested",t)

#############set################
s=set()
print("empty",s)
for i in range(1,6):
    s.add(i)
print(s)
s1=set()
for i in range(8,10):
    s1.add(i)
print(s1)


