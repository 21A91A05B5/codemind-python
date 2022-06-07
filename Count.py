n=int(input())
a=list(map(int,input().split( )))
ec=0
oc=0
for i in range(n):
    if(a[i]%2==0):
        ec+=1
    else:
        oc+=1
print(ec,oc)