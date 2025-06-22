class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Keep track of the number of the open and close brackets
        num_open = n
        num_close = n
        results = set()

        def helper(temp, num_open, num_close):
            # Return when we used up all the brackets
            if len(temp) >= n * 2:
                results.add("".join(temp))
                return
            
            # Append "(" first
            if num_open > 0:
                temp.append("(")
                num_open -= 1
                helper(temp, num_open, num_close)
                # backtrack
                temp.pop()
                num_open += 1
                
            # Append ")" only when there are more "(" in the temp array
            if num_open < num_close:
                num_close -= 1
                temp.append(")")
                helper(temp, num_open, num_close)
                # backtrack
                temp.pop()
                num_close += 1

        helper([], num_open, num_close)
        return list(results)
