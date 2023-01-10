class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # key : sorted chars - val = actual chars
        
        
        #k,n
        #klonk*n
        wordDict = {}
        
        for word in strs:
            keyword = "".join(sorted(word))  
            if keyword not in wordDict:
                wordDict[keyword] = []
            wordDict[keyword].append(word)
        
        return wordDict.values()
        
            
            
            
            
    
    
        
        