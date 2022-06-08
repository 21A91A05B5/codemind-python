n=int(input())
c=0
dc=0
a=list(map(int,input().split( )))
for i in range(len(a)):
    dc=0
    temp=a[i]
    while(temp):
        r=temp%10
        temp=temp//10
        dc+=1
    if dc%2==0:
        c+=1
print(c)