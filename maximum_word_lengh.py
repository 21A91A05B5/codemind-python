s=list(map(str,input().split( )))
c=[]
for i in range(len(s)):
    x=len(s[i])
    c.append(x)
print(max(c))