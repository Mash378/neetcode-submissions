class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        n=len(nums)
        dp = [0]*n

        def rob_linear(sub_nums: List[int]) -> int:
            if not sub_nums:
                return 0
            if len(sub_nums) == 1:
                return sub_nums[0]
            
            dp = [0] * len(sub_nums)
            dp[0] = sub_nums[0]
            dp[1] = max(sub_nums[0], sub_nums[1])
            
            for i in range(2, len(sub_nums)):
                dp[i] = max(dp[i-1], sub_nums[i] + dp[i-2])
                
            return dp[-1]

        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))