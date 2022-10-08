a=int(input())
x=list(map(int,input().split( )))
b=int(input())
y=list(map(int,input().split( )))
res=[None]
for i in range(a):
    res.insert(y[i],x[i])
for i in range(a):
    print(res[i],end=" ")