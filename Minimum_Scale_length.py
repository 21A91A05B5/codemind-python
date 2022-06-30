n=int(input())
l=list(map(int,input().split( )))
for i in range(1,100):
    c=0
    for j in range(n):
        if(l[j]%i==0):
            c+=1
    if(c==n):
        maxi=i
print(maxi)