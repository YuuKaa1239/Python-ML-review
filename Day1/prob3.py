get = int(input())

i=2
while i*i<=get:
    while get%i==0:
        print(i)
        get/=i
    i+=1

if get>1:
    print(int(get))
