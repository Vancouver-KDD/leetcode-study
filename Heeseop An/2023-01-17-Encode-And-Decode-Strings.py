class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s

        return encoded


    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """

        decoded = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            decoded.append(s[j + 1: j + 1 + length])
            i = j + 1 + length

        return decoded






# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))