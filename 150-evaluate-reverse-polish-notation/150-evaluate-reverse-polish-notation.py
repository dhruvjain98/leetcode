class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        for i in tokens:
            try:
                num = int(i)
                stack.append(int(i))
            except:
                v1 = stack.pop()
                v2 = stack.pop()
                
                if i == "+": stack.append(v2 + v1)
                if i == "-": stack.append(v2 - v1)
                if i == "*": stack.append(v2 * v1)
                
                # if i == "/": stack.append(int(v2 // v1))
                
                if i == "/":    # floor divide for negative numbers
                    if v1 < 0 or v2 < 0: stack.append(int(v2/v1))
                    else: stack.append(int(v2 // v1))
        return stack[-1]
            
            # To handle "-ve" numbers in the string. isnumeric checks if every char in string is numeric or not.
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