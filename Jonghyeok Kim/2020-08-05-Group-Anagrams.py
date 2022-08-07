class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for ch in strs:
            ch_copy = str(ch)
            ch_sorted = ''.join(sorted(ch_copy))
            if ch_sorted in hash_map:
                hash_map[ch_sorted].append(ch)
            else:
                hash_map[ch_sorted] = [ch]
        return hash_map.values()