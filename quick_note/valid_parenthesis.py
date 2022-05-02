class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')':'(', ']':'[', '}':'{'}
        for c in s:
            if c in pairs: # check wheter closing parenthesis (key)
                if stack and stack[-1] == pairs[c]: # not empty and top value
                    stack.pop()
                else:
                    return False
            else: # if open parenthesis, can add as many as we want
                stack.append(c)
        if stack: # if stack is not empty after the process
            return False
        else:
            return True