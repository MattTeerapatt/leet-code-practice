from typing import List

class Solution:

    #best case  = Hast Table = O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # create a empty hash table or dict for getting the the value 
        # after complete the diff = target - nums[i]
        seen = {} 

        for i in range(len(nums)):

            diff = target - nums[i]

            if diff in seen: #if diff is been in the array it will return the result
                #ex [2, 7, 11, 15] target = 9
                #{7: 0} because 9 - 2 = 7 and 2 is in the 0 index
                #the second one {7:0 , 2:1} because 9 - 7 = 2 and 7 is in the 1 index
                # in this case 2 is pair number 
                return [seen[diff], i]
            
            #collect diff in seen dict
            seen[nums[i]] = i
        return []
    

    #Bructe Force = O(n^2)
    # def twoSumBruteForce(self, nums: List[int], target: int) -> List[int]:
    #     for i in range(len(nums)):
    #         for j in range(len(nums)):
    #             if i != j and nums[i] + nums[j] == target:
    #                 return [i, j]
    #     return []

solution = Solution()

result = solution.twoSum(nums=[2, 7, 11, 15], target=17)
# result3 = solution.twoSum(nums=[3, 2, 4], target=6)
# result2 = solution.twoSum(nums=[3, 3], target=6)

print(result)
# print(result2)
# print(result3)
