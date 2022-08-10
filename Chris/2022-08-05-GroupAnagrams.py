class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        wordDict = {}
        
        
        for word in strs:
            sortedWord = ''.join(sorted(word))
            
            if sortedWord not in wordDict:
                wordDict[sortedWord] = [word]
            else:
                wordDict[sortedWord].append(word)

        
        
        return wordDict.values()
        
            
            
            
            
    
    
        
        