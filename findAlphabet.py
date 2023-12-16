class Solution:
    def findAlphabetsFromString(self, s: str) -> str:
        result = ""
        for char in s:
            # Check if the character is a letter (A-Z or a-z)
            if ('A' <= char <= 'Z') or ('a' <= char <= 'z'):
                result += char
        return result

solution = Solution()
s = "a1b2c3"
result = solution.findAlphabetsFromString(s)
print(f"Result: {result}")
