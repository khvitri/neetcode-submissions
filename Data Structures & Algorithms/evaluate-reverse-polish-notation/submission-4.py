class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Operators can take at most 2 operands
        operators = {"+", "-", "*", "/"}

        stack = []

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
                continue

            rOperand = stack.pop()
            lOperand = stack.pop()
            if token == "+":
                res = lOperand + rOperand
                stack.append(res)
            elif token == "-": 
                res = lOperand - rOperand
                stack.append(res)
            elif token == "*":
                res = lOperand * rOperand
                stack.append(res)
            else:
                res = int(lOperand / rOperand)
                stack.append(res)
        
        return stack[0]


            
