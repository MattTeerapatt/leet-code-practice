class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3:str) -> int:
        
        
        if not s1[0] == s2[0] == s3[0]:
            return -1
        
        minLen = min(len(s1), len(s2), len(s3))

        res = len(s1) + len(s2) + len(s3) 
        
        for i in range(minLen):
            if s1[i] == s2[i] == s3[i]:
                res -= 3
            else:
                break
        return res
    
solution = Solution()
result = solution.findMinimumOperations("b", "aba", "aaccaa")
print (result)