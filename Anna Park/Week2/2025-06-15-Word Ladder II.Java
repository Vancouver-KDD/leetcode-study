from collections import defaultdict, deque
from typing import List

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        
        # Step 1: BFS to build distance and neighbors
        neighbors = defaultdict(list)
        distance = {beginWord: 0}
        queue = deque([beginWord])
        
        while queue:
            current_word = queue.popleft()
            current_distance = distance[current_word]
            
            for next_word in self.getNextWords(current_word, wordSet):
                neighbors[current_word].append(next_word)
                if next_word not in distance:
                    distance[next_word] = current_distance + 1
                    if next_word == endWord:
                        continue
                    queue.append(next_word)
        
        # Step 2: DFS to build all shortest paths
        results = []
        self.dfs(beginWord, endWord, neighbors, distance, [beginWord], results)
        return results
    
    def getNextWords(self, word, wordSet):
        res = []
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if c != word[i]:
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in wordSet:
                        res.append(next_word)
        return res
    
    def dfs(self, current, endWord, neighbors, distance, path, results):
        if current == endWord:
            results.append(list(path))
            return
        
        for neighbor in neighbors[current]:
            if distance[neighbor] == distance[current] + 1:
                path.append(neighbor)
                self.dfs(neighbor, endWord, neighbors, distance, path, results)
                path.pop()
