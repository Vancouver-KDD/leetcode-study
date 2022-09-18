class Solution:

    delim = ":;"
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        res = ""
        passFirst = True
        
        for text in strs:
            if passFirst:
                passFirst = False
            else:
                res += self.delim
            res += text       
        return res

        

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        
        n = len(self.delim)
        res = []
        word = ""
        i = 0
        while i < len(str):
            if str[i:i+n] == self.delim:
                res.append(word)
                word = ""
                i += n
            else:
                word += str[i]
                i += 1
        if len(word) > 0:
            res.append(word)
        return res

