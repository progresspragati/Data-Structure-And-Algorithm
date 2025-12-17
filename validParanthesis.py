class Solution:
    def isValid(self, s: str) -> bool:
        bracket_stack = []
        for bracket in s:
            if bracket == '(':
                bracket_stack.append(bracket)
            elif bracket == '[':
                bracket_stack.append(bracket)
            elif bracket == '{':
                bracket_stack.append(bracket)
            elif len(bracket_stack) != 0:
                if bracket == ')' and bracket_stack[-1] == '(':
                    bracket_stack.pop()
                elif bracket == ']' and bracket_stack[-1] == '[':
                    bracket_stack.pop()
                elif bracket == '}' and bracket_stack[-1] == '{':
                    bracket_stack.pop()
                else:
                    bracket_stack.append(bracket)
            else:
                bracket_stack.append(bracket)
        if len(bracket_stack) == 0:
            return True
        return False
                
result = Solution()
print(result.isValid("[]"))    
# print(result.isValid("]"))    
