#not 100%

# class Solution:
#     def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
#         all_length =sorted([len(s1), len(s2), len(s3)])
#         print("all length" , all_length)   
#         min_length = all_length[0]
#         # print("min length" , min_length)


#         strings = [s1, s2, s3]

#         for i in range(3):
#             strings[i] = strings[i][0:min_length]

#         s1, s2, s3 = strings
#         print(s1, s2, s3)

#         # s1 = s1[0:min_length:1]
#         # s2 = s2[0:min_length:1] # [start:end:step]
#         # s3 = s3[0:min_length:1]
#         # print(s1, s2, s3)

#         #check string letter equivalent
#         count = 0
#         for i in range(min_length):
#             if s1[i] == s2[i] == s3[i]:
#                 count += 1
 
#             elif s1[1] != s2[1] != s3[1]:
#                 return -1
#         return count
    


class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3:str) -> int:
        if not s1[0] == s2[0] == s3[0]:
            return -1
        minLen = min(len(s1), len(s2), len(s3))

        result = len(s1) + len(s2) + len(s3) 
        for i in range(minLen):
            if s1[i] == s2[i] == s3[i]:
                result -= 3 # Decrement the sum by 3 for each matching character in the strings
            else:
                break # Break the loop when a mismatch is encountered
        return result

        
            




solution = Solution()
result = solution.findMinimumOperations("abc", "abcdefgef", "adc")
result = solution.findMinimumOperations("a", "a", "a")

# result = solution.findMinimumOperations("abc", "abb", "ab")
# result = solution.findMinimumOperations("dac", "bac", "cac")

print(result)