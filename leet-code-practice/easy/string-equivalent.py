from typing import List 

class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        return "".join(word1) == "".join(word2)


# word1 = ["ab", "c"]
# word2 = ["a", "bcs"]
word1  = ["abc", "d"]
word2 = ["abcd"]
solution = Solution()
result = solution.arrayStringsAreEqual(word1, word2)

print(result)