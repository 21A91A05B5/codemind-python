n=int(input())
l=list(map(int,input().split( )))
k=int(input())
s=[]
c=0
for i in l:
    if i not in s:
        s.append(i)
for i in s:
    if(l.count(i)==k):
        c+=1
        print(i,end=' ')
if(c==0):
    print("-1")