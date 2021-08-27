from array import *


n=int(input("Lungimea vectorului"))
x=array('i',[])
for i in range(0,n):
    k=int(input())
    x.append(k)
print(x)
for i in range(0,n-1):
    for j in range(i+1,n):
        if x[i]>x[j]:
            print(x[i],x[j])
            aux=x[i]
            x[i]=x[j]
            x[j]=aux

print(x)    