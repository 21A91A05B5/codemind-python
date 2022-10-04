s=list(map(str,input().split( )))
for i in s:
    k=ord(min(i))
    l=ord(max(i))
    print(l-k,end=" ")