s=list(map(str,input().split( )))
c=0
d=[]
for i in s:
    for j in i:
        if j=='a' or j=='e' or j=='i' or j=='o' or j=='u' or j=='A' or j=='E' or j=='I' or j=='O' or j=='U':
            c+=1
    d.append(c)
    c=0
print(*d)