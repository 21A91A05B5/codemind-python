a,b=map(int,input().split( ))
l=list(map(int,input().split( )))
c=0
for i in range(a):
    if l[i]>=b:
        c+=1
print(c)
    
    
    