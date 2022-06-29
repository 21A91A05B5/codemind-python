s=input()
flag=0
for c in s:
    if(s.count(c)>1):
        flag=1
        break
if(flag==0):
    print("True")
else:
    print("False")