class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_elems = []

        result = []
        for elem in strs:
            sorted_elem = sorted(elem)
            sorted_elems.append(tuple(sorted_elem))

        set_of_sorted_elems = set(sorted_elems)
        for sorted_elem in set_of_sorted_elems:
            sub = []
            result.append(sub)
            for compared_original, compared_sorted_elem in zip(strs, sorted_elems):
                if sorted_elem == compared_sorted_elem:
                    sub.append(compared_original)
        return result
