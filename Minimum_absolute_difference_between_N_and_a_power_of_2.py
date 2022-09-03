from math import floor,log2
n=int(input())
l=pow(2, floor(log2(n)))
p=l*2
k=min((n-l),(p-n))
print(k)