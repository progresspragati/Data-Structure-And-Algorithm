class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) % 2 == 1:
            return False
        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)
            elif ch == ')' and ((not stack )or (stack.pop() != '(')):
                return False
            elif ch == '}' and ((not stack) or (stack.pop() != '{')):
                return False
            elif ch == ']' and ((not stack) or (stack.pop() != '[')):
                return False
        if stack:
            return False
        return True
    
result = Solution()
print(result.isValid("[(])"))

