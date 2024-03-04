class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = j = 0
        while i < len(word) and j < len(abbr):
            num = 0
            if word[i] == abbr[j]:
                i += 1
                j += 1
                continue
            elif abbr[j].isdigit():
                if abbr[j] == '0':
                    return False                    
                while j < len(abbr) and abbr[j].isdigit():
                    num = num * 10 + int(abbr[j])                
                    j += 1                                    
                i += num
                if i > len(word):
                    return False   
                continue
            else:
                return False
        return i == len(word) and j == len(abbr)
                


        