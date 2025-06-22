class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Declare variables substring, longest substring, and each character of substring as a set
        substring, substring_max, substring_set = [], [], set()
        # Iterate over the given string once, one character at a time
        for char in s:
            # If substring already includes the character, compare length with longest substring
            if char in substring_set:
                # Update longest substring
                substring_max = substring if len(substring) > len(substring_max) else substring_max
                # Empty substring and substring set
                substring = substring[substring.index(char) + 1:]
                substring_set = set(substring)
            # Append character to substring and add character to substring set
            substring.append(char)
            substring_set.add(char)
        # Compare substring once more outside loop
        substring_max = substring if len(substring) > len(substring_max) else substring_max
        # Return the length of longest substring
        return len(substring_max)