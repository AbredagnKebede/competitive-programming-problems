class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for i in tokens:
            if i.lstrip('-').isdigit():
                stack.append(int(i))
                
            else:
                if i == "*":
                    op1 = stack.pop()
                    op2 = stack.pop()
                    stack.append(op1*op2)
                elif i == '/':
                    op1 = stack.pop()
                    op2 = stack.pop()
                    stack.append(int(op2/op1))
                elif i == '+':
                    op1 = stack.pop()
                    op2 = stack.pop()
                    stack.append(op1 + op2)
                elif i == '-':
                    op1 = stack.pop()
                    op2 = stack.pop()
                    stack.append(op2 - op1)

        return stack.pop()