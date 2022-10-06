n=int(input())
a=list(map(int,input().split( )))
z=0
for i in range(n):
    for j in range(i,n):
        if z<a[j]-a[i]:
            z=a[j]-a[i]
print(z)