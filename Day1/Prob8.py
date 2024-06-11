x = [int(x) for x in input().split()]
s ={0}
dic = dict()

for i in x:
    dic[i]=dic.get(i,0)+1
    s.add(i)
s.remove(0)
for i in s:
    if i%2!=0 and dic[i]%2!=0:
        print(i,dic[i])
