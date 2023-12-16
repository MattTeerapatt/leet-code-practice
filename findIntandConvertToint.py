from typing import List


# class Solution:
#     def findIntFromString(self, s: str) -> int:
#         result = ""
#         for char in s:
#             if char.isdigit():
#                 result += char
#         return int(result)
    


# solution = Solution()
# s = "a1b2c3"
# result = solution.findIntFromString(s)
# print(f"Result: {result}")
# # print(type(result))


################## 2 ##################
from typing import List

class Solution:
    def findIntegersFromString(self, s_list: List[str]) -> int:
        result = ""
        for s in s_list:
            for char in s:
                if '0' <= char <= '9':
                    result += char
        return int(result)
    
solution = Solution()
s = ["a1b234232c3", "a1b2c3"]
result = solution.findIntegersFromString(s)
print(f"Result: {result}")
print(type(result))






################## 3 ##################


# class Solution:
#     def findIntFromString(self, s: str) -> int:
#         result = ""
#         for char in s:
#             try:
#                 int_value = int(char)
#                 result += char
#             except ValueError:
#                 pass
#         return int(result)

# solution = Solution()
# s = "a1b2c3"
# result = solution.findIntFromString(s)
# print(f"Result: {result}")
# # print(type(result))
