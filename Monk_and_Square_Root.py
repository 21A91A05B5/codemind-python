import math
t=int(input())
ans=-1
for i in range(t):
    ans=-1
    a,b=map(int,input().split( ))
    for i in range(0,b):
       if(i*i)%b==a:
           ans=i
           break
    print(ans)
    