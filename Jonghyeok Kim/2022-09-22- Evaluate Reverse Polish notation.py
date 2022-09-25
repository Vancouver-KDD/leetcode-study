class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #post order tree
        op_hash = {"+":1,"*":1,"-":1,"/":1}
        stack = []
        # char -> operator
        def do_math(num1, num2, op):
            num1 = float(num1)
            num2 = float(num2)
            if op == "+":
                return num1 + num2
            elif op == "*":
                return num1 * num2
            elif op == "/":
                return trunc(num1 / num2)
            else:
                return num1 - num2
            
        for token in tokens:
            if token not in op_hash:
                stack.append(token)
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(do_math(num1,num2, token))
        return int(stack[0])