s=input()
s=s.lower()
s=list(s)
k=s.copy()
k=set(k)
k=list(k)
c=0
for i in range(len(k)):
    if(s.count(k[i])==1 and k[i]!=" "):
        c+=1
print(c)