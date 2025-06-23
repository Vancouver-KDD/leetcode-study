# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = [] 
#         pairs = {')':'(', '}':'{',']':'['}

#         for ch in s: 
#             if ch in pairs: 
#                 if not stack or pairs[ch] != stack.pop():              
#                     return False
#             else:
#                 stack.append(ch)

#         return not stack



class Solution: 
    def isValid(self, s: string) -> bool: 
        stack = []
        pairs = {')':'(', '}':'{',']':'['}

        for ch in s: 
            #({[
            if ch not in pairs:
                stack.append(ch)


            # }])
            else: 
                if not stack: 
                    return False 

                if stack.pop() != pairs[ch]:
                    return False

        if not stack:
            return  True
        else:
            return False                                           