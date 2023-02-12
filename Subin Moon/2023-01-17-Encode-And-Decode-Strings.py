# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.
# Please implement `encode` and `decode`

# Input: ["lint","code","love","you"]
# Output: ["lint","code","love","you"]
# Explanation:
# One possible encode method is: "lint:;code:;love:;you"

# Input: ["we", "say", ":", "yes"]
# Output: ["we", "say", ":", "yes"]
# Explanation:
# One possible encode method is: "we:;say:;:::;yes"

class Solution:
    # O(n^2) because the string concatenation copies the entire string, so the result string is being copied over and over n times
    def encode(self, strs):
        """
        @param strs: a list of strings
        @return: encodes a list of strings to a single string
        """
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def encode_O_n(self, strs):
        return "".join(f"{len(string)}#{string}" for string in strs)

    def decode(self, str):
        """
        @param str: a single string
        @return: decodes a single string to a list of strings
        """
        for c in str:
            res, i = [], 0

            while i < len(str):
                j = i
                while str[j] != "#":
                    j += 1
                length = int(str[i:j])  # integer, word length
                res.append(str[j+1:j+length+1])
                i = j + 1 + length

        return res
