n=int (input())
c=0
for i in range(1,n+1):
    if(n%1==0 and n%i==0):
        c=c+1
if(c==2):
    print("prime")
else:
    print("not a prime")
    
