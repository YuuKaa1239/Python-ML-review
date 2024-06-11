f = [1,1]
sum=2
n=int(input())

i=2
while i<=n:
    f.append(f[i-1]+f[i-2])
    sum+=f[i]
    i+=1

print(sum)
