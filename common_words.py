a=list(map(str,input().lower().split( )))
b=list(map(str,input().lower().split( )))
for i in b:
    if i in a:
        print(i,end=" ")
        