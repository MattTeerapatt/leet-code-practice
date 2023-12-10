from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        for right in range(len(nums)):
            print("time -------", right)
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
            print("left = ",left)
            print("right = ",right, " \n")
            print(nums," \n")
        return left
            
    
solution = Solution()
nums = [0,1,2,2,3,0,4,2]
val = 3
result = solution.removeElement(nums, val)
print(f"Result: {result}, nums = {nums[:result]}")# [start:end:step]
         