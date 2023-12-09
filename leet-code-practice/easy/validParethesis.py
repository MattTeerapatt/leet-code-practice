#stack pop last in first out LIFO

class Solution:
    def isValid(self, s : str) -> bool:
        stack = []
        for char in s:
            if char in [ "(", "{", "[" ]:
                stack.append(char)  #keep left ( [ {parenthesis in stack [] 
                #right parenthesis ) ] } still in char
            else:
                if not stack: #if stack is empty
                    return False
                current_char = stack.pop() # pop the last element in stack to check with  prenthesis in char
                if current_char == "(":
                    if char != ")":
                        return False
                if current_char == "{":
                    if char != "}":
                        return False
                if current_char == "[":
                    if char != "]":
                        return False #stack suppose to be empty if all parenthesis match
        if stack: #if stack is not empty (remain some pair of parenthesis)
            return False
        return True



solution = Solution()
result = solution.isValid("()[]{}")
print(result)