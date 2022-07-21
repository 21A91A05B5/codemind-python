s=input()
v="aeiouAEIOU"
l=[]
c=0
for i in s:
    if i in v and i not in l:
        l.append(i)
print(*l)
