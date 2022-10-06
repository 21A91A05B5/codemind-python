def prime(x):
    if(x==1):
        return 0
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return 0
    return 1
n=int(input())
c=0
for i in range(1,n):
    if(n%i==0):
        if prime(i):
            print(i,end=" ")
            c+=1
if(c==0):
    print("-1")