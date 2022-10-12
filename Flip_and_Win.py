n=int(input())
a=input()
s=0
for i in range(0,n-1):
    s+=abs(int(a[i+1])-int(a[i]))
s=n-1-s
if(s%3==0):
    print("Sudhir")
else:
    print("Ashok")
