from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #find min length 
        min_length = min([len(s) for s in strs]) if strs else 0
        if strs:
             min_length = min([len(s) for s in strs])
        else: 
            return ""
        # print(min_length)

        #find common prefix
        common_prefix =""
        for i in range(min_length):
            if all([s[i] == strs[0][i] for s in strs]):
                common_prefix += strs[0][i]
                # print(common_prefix)
            else:
                break
        return common_prefix


Solution = Solution()
result = Solution.longestCommonPrefix(["flower","flow","flight","flight"])
print(result)