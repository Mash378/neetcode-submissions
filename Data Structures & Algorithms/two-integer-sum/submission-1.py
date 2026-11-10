class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Map = {}

        for i in range(len(nums)):
            
            remaining = target - nums[i]
            if nums[i] in Map:
                return [Map[nums[i]], i]
            Map[remaining]=i
        
        return []