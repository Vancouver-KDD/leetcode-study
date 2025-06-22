"""
String Encode and Decode
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Constraints:

0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains only UTF-8 characters.

python hye/2024-10-03-string-encode-and-decode.py
"""

from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s)) + "#" + s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        index = 0
        results = []
        size = len(s)
        while index < len(s):
            last_index = index
            while last_index < size and s[last_index] != "#":
                last_index += 1
            length = int(s[index:last_index])
            index = last_index + 1
            last_index = index + length
            results.append(s[index:last_index])
            index = last_index
        return results


def test_handler(s, input):
    print("\nTest with Input: ", input)
    encoded_str = s.encode(input)
    print("encoded_str: ", encoded_str)
    decoded_stor = s.decode(encoded_str)
    print("decoded_stor: ", decoded_stor)
    assert input == decoded_stor
    print()

def main():
    s = Solution()

    input = ["neet","code","love","you"]
    test_handler(s, input)
    input = ["we","say",":","yes"]
    test_handler(s, input)
    input = [""]
    test_handler(s, input)
    input = []
    test_handler(s, input)
    input = ["we","say",":","yes","!@#$%^&*()"]
    test_handler(s, input)

    print("Success!")
    
if __name__ == "__main__":
    main()
