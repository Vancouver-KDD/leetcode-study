class Solution:
    def isPalindrome(self, s: str) -> bool:

        # returns ture if string(s) is empty.
        if s == "":
            return True

        # initiate results to compare.
        res1 = ""
        res2 = ""

        # convert all characters of s into lower-case.
        lowered_s = s.lower()

        # iterate s forwards.
        for char in lowered_s:
            # append letters and digits only
            if char.isalnum():
                res1 += char

        # iterate s backwards.
        for char in lowered_s[::-1]:
            # append letters and digits only
            if char.isalnum():
                res2 += char

        if res1 == res2:
            return True

# Time complexity:
# Space complexity: