n=int(input( ))
sum=0
r1=0
r2=0
sq1=n*n
while(n>0):
    r1=r1*10
    r1=r1+n%10
    n=n//10
sq2=r1*r1
while(sq2>0):
    r2=r2*10
    r2=r2+sq2%10
    sq2=sq2//10
if(sq1==r2):
    print("True")
else:
    print("False")