from typing import List

class Solution:

    def bubbleSort(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums) - 1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]

        return nums

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = self.bubbleSort(nums1 + nums2)
        length = len(merged)

        if length % 2 == 0:
            m = length // 2
            n = length // 2 - 1
            return (merged[n] + merged[m]) / 2
        else:
            return merged[length // 2]
        

num1 = [1,2,6]
num2 = [3,4]

solution = Solution()
nums = solution.bubbleSort(num1 + num2)
result = solution.findMedianSortedArrays(num1, num2)
print(nums , "\n")
# print(result)


        