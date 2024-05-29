class Solution:
    def jump(self, nums):
        i = 0
        jump = 0
        if not nums or len(nums) == 1:
            return 0
        
        next_idx = 0
        while True:
            i = next_idx
            jump += 1
            max_val = 0
            if nums[i] >= (len(nums)-i-1):
                break
            for j in range(nums[i], 0, -1):
                if j+nums[i+j] > max_val:
                    next_idx = (i+j)
                    max_val = j+nums[i+j]
        return jump
    # def jump(self, nums: List[int]) -> int:
    #     jump = 0
    #     n = len(nums)
    #     if n == 1:
    #         jump = 0
    #         return jump
    #     pos = 0
    #     while True:
    #         jump += 1
    #         cVal = nums[pos]
    #         if cVal + pos >= n-1:
    #             break
    #         cMax = 0
    #         maxPos = pos
    #         for i in range(cVal):
    #             tempPos = i+1+pos 
    #             tempVal = nums[tempPos]
    #             if tempVal + i > cMax:
    #                 maxPos = tempPos
    #                 cMax = tempVal + i
    #     return jump