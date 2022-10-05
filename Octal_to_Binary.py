n=int(input())
for i in range(n):
    a=int(input())
    sum=0
    i=0
    while a!=0:
        j=a%10
        sum+=j*(8**i)
        a//=10
        i+=1
    print('{0:b}'.format(sum))