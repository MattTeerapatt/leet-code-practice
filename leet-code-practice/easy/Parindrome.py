class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        div = 1
        while x > 10 * div:
            div *= 10
        while x:
            right = x % 10
            left = x // div

            print(f"x: {x}, div: {div}, left: {left}, right: {right}")

            if left != right:
                return False
            # print(x % div)
            x = (x % div) // 10  #remove left digit then // remove right
            # print(f"new x: {x}")
            div = div // 100
        
        return True

solution = Solution()
result = solution.isPalindrome(3456543)
print(result)
