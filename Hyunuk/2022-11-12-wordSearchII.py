class TrieNode:
    
    def __init__(self):
        self.children = dict()
        self.end_of_word = False
        
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def _search_prefix(self, word):
        node = self.root
        for c in word:
            if not node.children.get(c):
                return False
            node = node.children[c]
        return node
    
    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.end_of_word = True

    def search(self, word: str) -> bool:
        node = self._search_prefix(word)
        return node and node.end_of_word

    def startsWith(self, prefix: str) -> bool:
        return bool(self._search_prefix(prefix))

    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def is_valid(y, x):
            return y >= 0 and x >= 0 and y < r and x < c
        
        def backtrack(y, x, sub):
            sub_str = ''.join(sub)
            if (y, x) not in seen and trie.startsWith(sub_str):
                if sub_str in words_set:
                    ret.append(sub_str)
                    words_set.remove(sub_str)
                
                for direction in directions:
                    dy, dx = direction
                    if not is_valid(y+dy, x+dx):
                        continue
                    seen.add((y, x))
                    sub.append(board[y+dy][x+dx])
                    backtrack(y+dy, x+dx, sub)
                    sub.pop()
                    seen.remove((y, x))
                return
            
        if not board or not board[0]:
            return []
        ret = []
        trie = Trie()
        seen = set()
        words_set = set(words)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for word in words:
            trie.insert(word)
        r = len(board)
        c = len(board[0])
        for i in range(r):
            for j in range(c):
                if not words_set:
                    return ret
                if trie.startsWith(board[i][j]):
                    backtrack(i, j, [board[i][j]])
        return ret
