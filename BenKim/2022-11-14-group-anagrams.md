# 49. Group Anagrams

> Problem link: https: https://leetcode.com/problems/group-anagrams/  
> submission detail: https://leetcode.com/problems/group-anagrams/submissions/843017250/  

```py
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 초기값을 []로 같는 dict를 생성한다
        anagrams = collections.defaultdict(list)

        # sort메서드로 정렬된값을 key로, 원래값을 value로 삽입한다
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagrams[sorted_word].append(word)
            
        # values()를 통해 리스트들을 리턴한다
        return anagrams.values()
```