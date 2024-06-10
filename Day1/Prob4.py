x = [int(x) for x in input().split()]

dp=[1]*len(x)
for i in range(1,len(x)):
    for j in range(0,i):
        if x[i]>x[j] and dp[i]<dp[j]+1:
            dp[i]=dp[j]+1

print(dp[len(dp)-1])
