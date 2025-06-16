class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Convert the given string into all lowercase alphanumeric characters
        characters = []
        for char in s:
            if char.isalnum():
                characters.append(char.lower())
        converted_s = "".join(characters)
        # Implement two index points on each end of the string
        lower, upper = 0, len(converted_s) - 1
        # Iterate through the string from two indices
        while lower < upper:
            # Check if characters match
            if converted_s[lower] != converted_s[upper]:
                # Return false if characters do not match, thus not a palindrome
                return False
            # Incrementing lower and decrement upper
            lower += 1
            upper -= 1
        # Return true if palindrome
        return True