x=list(map(str,input().lower().split( )))
y=list(map(str,input().lower().split( )))
c=0
a=[]
b=[]
for i in x:
    if(y.count(i)==1):
        a.append(i)
for i in y:
    if x.count(i)==1:
        b.append(i)
for i in a:
    if i in b:
        c+=1
print(c)