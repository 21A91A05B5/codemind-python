s=input()
c=[]
d=[]
for i in s:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        c.append(i)
    elif i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
        d.append(i)
k=len(set(c))
l=len(set(d))
if(k==5 or l==5):
    print("True")
else:
    print("False")