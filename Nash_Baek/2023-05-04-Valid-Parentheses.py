# For more description, please visit the blog below.
# https://peterdrinker.tistory.com/478

class Solution:
    def isValid(self, s: str) -> bool:
        # Error handling part
        # 1. It checks the length of string.And the length has to be even number.
        # 2. It checks whether the string contains parentheses or not.
        list_of_string = list(s)
        length_of_string = len(list_of_string)
        if length_of_string % 2 != 0:
            return False

        stack = []
        # It uses stack data structure by matching characters.
        # Change the status of opened or closed by boolean variable for three parentheses.
        # The time complexity is O(N).
        
        cnt = length_of_string / 2
        for i in range(length_of_string - 1):
            if len(list_of_string) == 0:
                break

            if list_of_string[-1] == ')':
                stack.append(list_of_string.pop(-1))
                if list_of_string and list_of_string[-1] == '(':
                    del list_of_string[-1]
                    del stack[-1]
                    continue                    
                elif not list_of_string:
                    continue
                else:
                    stack.append(list_of_string.pop(-1))

            elif list_of_string[-1] == '(':
                if stack and stack[-1] == ')':
                    del list_of_string[-1]
                    del stack[-1]
                    continue
                elif not list_of_string:
                    continue
                else:
                    stack.append(list_of_string.pop(-1))
            
            elif list_of_string[-1] == '}':
                stack.append(list_of_string.pop(-1))
                if list_of_string and list_of_string[-1] == '{':
                    del list_of_string[-1]
                    del stack[-1]
                    continue
                elif not list_of_string:
                    continue
                else:
                    stack.append(list_of_string.pop(-1))

            elif list_of_string[-1] == '{':
                if stack and stack[-1] == '}':
                    del list_of_string[-1]
                    del stack[-1]
                    continue
                elif not list_of_string:
                    continue
                else:
                    stack.append(list_of_string.pop(-1))

            elif list_of_string[-1] == ']':
                stack.append(list_of_string.pop(-1))
                if list_of_string and list_of_string[-1] == '[':
                    del list_of_string[-1]
                    del stack[-1]
                    continue
                elif not list_of_string:
                    continue
                else:
                    stack.append(list_of_string.pop(-1))

            elif list_of_string[-1] == '[':
                if stack and stack[-1] == ']':
                    del list_of_string[-1]
                    del stack[-1]
                    continue
                elif not list_of_string:
                    continue
                else:
                    stack.append(list_of_string.pop(-1))

        return len(list_of_string) == 0 and len(stack) == 0

# solution = Solution()
# str = "}]}()){{)[{[(]"
# print(solution.isValid(str))
