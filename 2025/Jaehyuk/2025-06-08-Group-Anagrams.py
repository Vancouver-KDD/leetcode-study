from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ans = defaultdict(list)

        for s in strs:
            ans[str(sorted(s))].append(s)
        
        return list(ans.values())
    
    
sol = Solution()
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

#time complexity = O(n * k log k) n is the length of the strs 
# and k is length of the individual string
#space complexity = O(n * k)


#more efficient solution
class Solution2:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ans = defaultdict(list)

        for s in strs:
            count = [0] * 26 

            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[(str(count))].append(s)

        return list(ans.values())

#time complexity = O(n * k) where n is length of strs and k is number of characters in the string
#space complexity = O(n * k)