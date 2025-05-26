class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ""
        for word in strs:
            res += str(len(word))
            res += "#"
            res += word
        return res

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        i = 0
        length = ""
        while i < len(s):
            if s[i] == "#":
                word = s[i+1:i+int(length)+1]
                res.append(word)
                i += (int(length) + 1)
                length = ""

            else:
                length += s[i]
                i += 1

        return res
