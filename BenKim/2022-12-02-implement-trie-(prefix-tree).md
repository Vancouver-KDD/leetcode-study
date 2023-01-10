# 208. Implement Trie (Prefix Tree)

> Problem link: https://leetcode.com/problems/implement-trie-prefix-tree/  
> Submission detail: https://leetcode.com/problems/implement-trie-prefix-tree/submissions/853169456/     

- Trie는 문자열을 저장하고 효율적으로 탐색하기 위한 트리 형태의 자료구조이다
- 자동완성 기능, 사전 검색 등 문자열을 탐색하는데 특화되어있는 자료구조이다
- startsWith가 trie 자료구조의 가장 큰 강점이다.

```py
class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.isEndOfWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]     
        curr.isEndOfWord = True

    def search(self, word: str) -> bool:
        
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]

        return curr.isEndOfWord
        

    def startsWith(self, prefix: str) -> bool:
        
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]

        return True        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
```