n=a = int(input())
s=""
if (1<=n<=10**6):
    while n!=1:
        if n%2:
            n=3*n+1
        else:
            n//=2
        s+=str(n)+" "
print(str(a), s)