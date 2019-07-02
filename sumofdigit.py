m=int(input())
s=0
i=0
while(m>0):
    i=m%10
    m=m//10
    s=s+i
print(s)
