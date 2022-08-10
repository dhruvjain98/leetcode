class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        paren = {')': '(', '}': '{', ']': '['}
        
        for c in s:
            if c not in paren:      # if char is OPEN
                stack.append(c)
                # print("stack app: {}".format(stack))
                continue
                
            if not stack or stack[-1] != paren[c]:
                return False
            
            stack.pop()
        
        return not stack
            
