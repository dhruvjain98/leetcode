class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        
        for i in tokens:
            # print(i)
            
            try:
                num = int(i)
                stack.append(int(i))
            except:
                # print("Stack: {}: {}".format(stack, i))
                v1 = stack.pop()
                v2 = stack.pop()
                if i == "+": stack.append(v2 + v1)
                if i == "-": stack.append(v2 - v1)
                if i == "*": stack.append(v2 * v1)
                # if i == "/": stack.append(int(v2 // v1))
                if i == "/":
                    if v1 < 0 or v2 < 0: stack.append(int(v2/v1))
                    else: stack.append(int(v2 // v1))
            
            
            
            # if i.isnumeric():
            #     stack.append(int(i))
            
            # else:
            #     print("Stack: {}".format(stack))
            #     v1 = stack.pop()
            #     v2 = stack.pop()
            #     if i == "+": stack.append(v2 + v1)
            #     if i == "-": stack.append(v2 - v1)
            #     if i == "*": stack.append(v2 * v1)
            #     if i == "/": stack.append(v2 // v1)
                    
        return stack[-1]