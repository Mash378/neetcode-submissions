class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Map = {}

        for i in range(len(nums)):
            remaining = target - nums[i]

            if remaining in Map:
                return [Map[remaining], i]
            Map[nums[i]] = i
        
        return []