from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        nums.insert(left, target)
        return left

solution = Solution()
nums = [1, 3, 5, 6]
target = 9
result = solution.searchInsert(nums, target)
print(f"Result: {result}")
