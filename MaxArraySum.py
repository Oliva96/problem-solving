def maxSubsetSum(arr):
    if len(arr) == 1:
        return max(arr[0], 0)
    
    dp0 = arr[0]
    dp1 = max(arr[0], arr[1])
    
    for i in range(2, len(arr)):
        current = max(dp0 + arr[i], dp1, arr[i])
        dp0, dp1 = dp1, current
    
    return max(dp1, 0)