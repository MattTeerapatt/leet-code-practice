# from typing import List

# class Solution:
#     def findPeaks(self, mountain: List[int]) -> List[int]:
#         left = 1
#         right = len(mountain) - 2  

#         peaks = []

#         while left <= right:
#             if mountain[left] > mountain[left - 1] and mountain[left] > mountain[left + 1]:
#                 peaks.append(left)
#             left += 1

#         return peaks

# solution = Solution()
# result = solution.findPeaks([10,6,8,4,5,3,1])
# print(result)


from typing import List

class Solution:
    def findPeakElement(self, mountain: List[int]) -> List[int]:
        left = 1
        right = len(mountain) - 2  # Excluding the first and last elements
        peaks = []

        while left <= right:
            if mountain[left] > mountain[left - 1] and mountain[left] > mountain[left + 1]:
                peaks.push(mountain[left])
            left += 1

        return peaks
    
solution = Solution()
result = solution.findPeakElement([10,6,8,4,5,3,1])
print(result)






