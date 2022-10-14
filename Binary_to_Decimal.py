t=int(input())
for i in range(t):
    n=int(input())
    dec=0
    i=0
    while(n):
        d=n%10
        dec=dec+d*pow(2,i)
        n=n//10
        i+=1
    print(dec)