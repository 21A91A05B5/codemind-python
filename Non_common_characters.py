a=input().lower()
b=input().lower()
l=[]
c=0
for i in a:
    if i not in b:
        l.append(i)
for i in b:
    if i not in a:
        l.append(i)
for j in sorted(set(l)):
    if j!=" ":
        c+=1
print(c)