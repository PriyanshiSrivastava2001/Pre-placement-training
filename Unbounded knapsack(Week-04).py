def unboundedKnapsack(W, n, val, wt):
    dp = [0 for i in range(W + 1)]
    ans = 0
    for i in range(W + 1): 
        for j in range(n): 
            if (wt[j] <= i): 
                dp[i] = max(dp[i], dp[i - wt[j]] + val[j]) 
  
    return dp[W] 

W = 100
val = [10, 30, 20] 
wt = [5, 10, 15] 
n = len(val) 
  
print(unboundedKnapsack(W, n, val, wt)) 


'''OUTPUT-
300
'''
