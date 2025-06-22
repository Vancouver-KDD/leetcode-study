class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        prefix, suffix = Trie(), Trie()
        count, res = defaultdict(int), 0
        for word in words:
            indicesPrefix = prefix.insert(word)
            indicesSuffix = suffix.insert(word[::-1], True)
            for chars in indicesPrefix:
                if chars in indicesSuffix:
                    res += count[chars]
            count[word] += 1
        return res

class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word: str, reverse = False) -> Set[str]:
        curChars, indices = self.root, set()
        for char in word:
            if char in curChars:
                curChars = curChars[char]
            else:
                curChars[char] = {}
                curChars = curChars[char]
            if 'end' in curChars:
                indices.add(curChars['end'])
        curChars['end'] = word if not reverse else word[::-1]
        return indices
