class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        operators = "+-*/"
        for i in tokens:
            if i not in operators:
                stk.append(int(i))
            else:
                op = i
                second = stk.pop()
                first = stk.pop()
                if op == "+":
                    res = first + second
                elif op == "-":
                    res = first - second
                elif op == "*":
                    res = first * second
                elif op == "/":
                    res = int(first / second)
                stk.append(res)
        return int(stk[0])
