class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anas = {} #dictionary saving words
        characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        word_length = len(strs[0])
        res = []
        sf = 0
        
        for word in strs:
            index = 0
            for j in range(len(word)):
                index += 26**characters.index(word[j])
                
            if index in anas.keys():
                res[anas[index]].append(word)
            else:
                anas[index] = sf
                sf += 1
                res.append([word])
        
        return res