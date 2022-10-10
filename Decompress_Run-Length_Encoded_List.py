n=int(input())
a=list(map(int,input().split( )))
for i in range(0,n,2):
    p=a[i]
    q=a[i+1]
    for i in range(p):
        print(q,end=" ")
        
    
        
    
    