class Solution:
    def totalMoney(self, n: int) -> int:
        ans = 0
        offset = 0
        for i in range(1, n + 1):
            #
            day = i % 7
            if day % 7 == 0:
                day += 7

            ans += offset + day

            #handle offset week 
            if i % 7 == 0:
                offset += 1

            print(f"i = {i}:")
            print(f"  res = {i} % 7 = {day}")
            print(f"  ans += {offset} + {day} = {ans}")
            print(f"  offset remains {offset}.\n")        


solution = Solution()
result = solution.totalMoney(12)  
print(result)
