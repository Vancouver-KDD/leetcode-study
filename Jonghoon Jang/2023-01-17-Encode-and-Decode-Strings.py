"""
271. Encode and Decode Strings

Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is
decoded back to the original list of strings.
"""


class Codec:

    def encode(self, strs: list[str]) -> str:
        return chr(257).join(strs)


    def decode(self, s: str) -> list[str]:
        if s == "":
            return [""]
        return s.split(chr(257))


def main():
    codec = Codec()
    print(codec.decode(codec.encode(["Hello","World"])))
    print(codec.decode(codec.encode([""])))
    print(codec.decode(codec.encode(["",""])))
    print(codec.decode(codec.encode([","])))
    print(codec.decode(codec.encode(["","4 "])))


if __name__ == "__main__":
    main()
