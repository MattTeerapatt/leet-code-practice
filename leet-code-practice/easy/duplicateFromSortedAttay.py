from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1
        for right in range(1, len(nums)): # right increment by 1 every time 
            if nums[right] != nums[right - 1]: 
                nums[left] = nums[right] # left value beome right value
                left += 1 # left increment by 1 when found the new value
        return left # return the length of the new array



solution = Solution()
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
result = solution.removeDuplicates(nums)
print(f"Result: {result}, nums = {nums[:result]}")# [start:end:step]
