n=int(input())
a=list(map(int,input().split( )))
m=a[0]
i=0
j=1
while(j<n):
    if(a[j]%m==0):
        j+=1
    else:
        m=a[j]%m
        i+=1
print(m)