class Solution:
    def strStr(self,heystack: str, needle: str) -> int:
        if needle == "":
            return -1
        if needle in heystack:
            return heystack.index(needle)
        return -1



solution = Solution()
heystack = "leetcode"
needle = "leeto"
result = solution.strStr(heystack, needle)
print(f"Result: {result}")# [start:end:step]