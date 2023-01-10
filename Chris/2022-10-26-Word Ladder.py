class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:   
        if endWord not in wordList:
            return 0
        
        nei = collections.defaultdict(list)
        # Add beginWord to the list as a beginning point of traversal
        wordList.append(beginWord)
        
        # Map each word to all possible patterns of the word
        # e.g. Map word "hot" to "*ot", "h*t", and "ho*"
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                nei[pattern].append(word)
        
        
        visit = set([beginWord])
        q = deque([beginWord])
        res = 1
        #BFS
        while q:
            for i in range(len(q)):
                word = q.popleft()
                # Got to the destination node
                if word == endWord:
                    return res
                # try to visit all neighbors current word
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j +1:]
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
            
            # increament the distance after each round of visit
            res += 1
        
        # When there is no endWord we are searching after visiting all nodes in the graph
        return 0
                
                
        
        
                
                
                
            