n=int(input())
for i in range(0,2**n):
    a=bin(i)[2:]
    print(str(a).zfill(n))