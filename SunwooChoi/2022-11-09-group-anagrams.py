class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_dict = {}
        result = []
        
        for s in strs:
            # sort string and use it as key
            sorted_s = ''.join(sorted(s))
            if sorted_s in group_dict:
                group_dict[sorted_s] = group_dict[sorted_s] + [s]
            else:
                group_dict[sorted_s] = [s]
        
        # extract item and append them to the result list
        for _, group in group_dict.items():
            result.append(group)
            
        return result

