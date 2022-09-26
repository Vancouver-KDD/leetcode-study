class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operators = ["+", "-", "*", "/"]
        stack = []
        for t in tokens:
            
            if t in operators:
                second = stack.pop()
                first = stack.pop()
                if t == "+":
                    result = first + second
                elif t == "-":
                    result = first - second
                elif t == "*":
                    result = first * second
                else:
                    result = int(first / second)
                
                stack.append(result)
            else:
                stack.append(int(t))
                
        return stack.pop()
            
            