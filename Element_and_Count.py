n=int(input())
l=list(map(int,input().split( )))
s=[]
for i in range(len(l)):
    if l[i] not in s:
        s.append(l[i])
for i in s:
    print(i,end=' ')
    print(l.count(i),end=' ')