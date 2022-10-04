a=list(map(str,input().lower().split( )))
b=list(map(str,input().lower().split( )))
c=0
for i in a:
    if i in b:
        c+=1
if(c>0):
    print(c)