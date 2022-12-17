# 198. House Robber
# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed,
# the only constraint stopping you from robbing each of them is that
# adjacent houses have security systems connected and it will automatically contact
# the police if two adjacent houses were broken into on the same night.
# Given an integer array nums representing the amount of money of each house,
# return the maximum amount of money you can rob tonight without alerting the police.


#     not good
class Solution:
    def rob(self, nums: List[int]) -> int:
        leng = len(nums)
        def maxProfit(nums, i):
            if i >= leng:
                return 0
            take =  nums[i] + maxProfit(nums, i+2)
            dont =  maxProfit(nums, i+1)
            return max(take, dont)
        return maxProfit(nums, 0)

# good
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        nums[1] = max(nums[0], nums[1])
        i = 2
        while i < len(nums):
            nums[i] = max(nums[i-1], nums[i] + nums[i-2])
            i += 1
        return nums[len(nums)-1]



# best ans:
class Solution:
    def rob(self, nums):
        a = b = 0
        for n in nums:
            a, b = b, max(b, n+a)
        return b