m=(input())
alp=0
dig=0
for i in m:
    if(i.isalpha()):
        alp=1
    if(i.isdigit()):
        dig=1
if(alp and dig==1):
        print('Yes')
else:
        print('No')
