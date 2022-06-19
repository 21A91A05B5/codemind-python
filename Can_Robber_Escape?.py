n=int(input())
o=0
a=list(map(int,input().split( )))
for i in range(n):
    if(a[i]%2!=0):
        o+=1
if o<=2:
    print("YES")
else:
    print("NO")