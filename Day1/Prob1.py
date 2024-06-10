import time

birth = str(input("format dd/mm/yyyy: "))

yy = int(time.strftime('%Y'))
mm = int(time.strftime('%m'))
dd = int(time.strftime('%d'))

split = []
temp=""

birth +='/'
for x in birth:
    if x=='/':
        split.append(int(temp))
        temp=""
    else:
        temp +=x

ans=yy-split[2]
if mm<split[1]:
    ans -=1
elif mm==split[1] and dd<split[0]:
    ans -=1

print(ans)
