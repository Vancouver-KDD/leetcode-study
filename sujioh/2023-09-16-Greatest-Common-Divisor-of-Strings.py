class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 == str2 + str1:
            divisor = min(len(str1), len(str2))
            while divisor > 0:
                if len(str1) % divisor == 0 and len(str2) % divisor == 0:
                    break
                divisor -= 1
            return str1[:divisor]
        else:
            return ""


'''
Summary:

Complexity:
 - Time: O(N) N is min(len(str1), len(str2))
 - Space: O(1)
 
 
1. Check if concatenating str1 and str2 is equal to concatenating str2 and str1, 
    which tests for a potential common divisor pattern.
2. If the concatenation is equal, find the greatest common divisor (GCD) of the strings' lengths 
    by iteratively decreasing a divisor from the minimum of the two lengths.
'''
