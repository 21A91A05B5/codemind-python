x=list(map(str,input().split( )))
y=list(map(str,input().split( )))
a=0
c=[]
d=[]
for i in x:
    if y.count(i)==1:
        c.append(i)
for i in y:
    if x.count(i)==1:
        d.append(i)
for i in c:
    if i in d:
        a+=1
print(a)
        