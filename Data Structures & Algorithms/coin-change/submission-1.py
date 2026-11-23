class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount+1)
        #Base case
        dp[0]=0

        #Recursive case
        for change in range(amount+1):
            for coin in coins:
                if change<coin:
                    continue
                
                dp[change] = min(dp[change-coin]+1, dp[change])
        
        return -1 if dp[amount]==float('inf') else dp[amount]