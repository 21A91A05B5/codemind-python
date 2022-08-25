s=input()
sp=0
for i in range(0,len(s)):
    if(s[i].isalpha()):
        continue
    elif(s[i].isdigit()):
        continue
    elif(s[i]==' '):
        continue
    else:
        sp+=1
if(sp>0):
    print(sp)
else:
    print("0")