s=input()
c=0
c1=0
for i in s:
    if i=='z':
        c+=1
    else:
        c1+=1
if(c*2==c1):
    print("Yes")
else:
    print("No")