def isPrime(n):
    if n<2:
        return False
    i=2
    while i*i<=n:
        if n%i==0:
            return False
        i+=1
    return True

def is_Perfect(n):
    for x in range(2,34,1):
        if isPrime(x):
            temp=pow(2,x)-1
            if isPrime(temp):
                temp1=pow(2,x-1)
                if temp*temp1==n:
                    return True
    return False

get = int(input())

if is_Perfect(get):
    print("YES")
else:
    print("NO")
