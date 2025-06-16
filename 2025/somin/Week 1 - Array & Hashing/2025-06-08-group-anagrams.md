

[LeetCode 49] Group Anagrams (Java)
https://leetcode.com/problems/group-anagrams/


```java
import java.util.*;

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> anagramMap = new HashMap<>();
        for(String str : strs ){
          char[] chars = str.toCharArray();
          Arrays.sort(chars);
          String sortedKey = new String(chars);
          if(anagramMap.containsKey(sortedKey)){
            anagramMap.get(sortedKey).add(str);
          }else{
            List<String> anagramList = new ArrayList<>();
            anagramList.add(str);
            anagramMap.put(sortedKey, anagramList);
          }
        }
        
        return new ArrayList<>(anagramMap.values());
    }
}

```

Time   : O(n \* m log m) 

Space  : O(n \* m)      

- Sorting each string takes O(m log m).
- Doing it for all n strings results in O(n * m log m).
- We store each string in a list grouped by key, leading to O(n * m) space.
