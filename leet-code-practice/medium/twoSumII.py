from typing import List

class Solution:
    def twoSum(self, numbers : List[int], target:int ) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right: # prevent to be out of range
            Current_Sum = numbers[left] + numbers[right]
            if Current_Sum > target: 
                right -= 1  #shift right index by -1
            elif Current_Sum < target: #shift left index by +1  
                left += 1 
            elif Current_Sum == target:
                return [left+1,right+1]
        return Current_Sum
                
        
solution = Solution()
result = solution.twoSum([2,7,11,15],9)
print (result)

            
            

            
