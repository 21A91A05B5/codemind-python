n=int (input())
temp=n
c=1
s=n*n
while(n!=0):
    c=c*10
    n=n//10
if(s%c==temp):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")