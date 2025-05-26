class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for word in strs:
            sorted_word = tuple(sorted(word))
            seen[sorted_word].append(word)

        return seen.values()