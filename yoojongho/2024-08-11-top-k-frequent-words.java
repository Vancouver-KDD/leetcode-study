/**
 * Leetcode
 * problem: 692
 * link: https://leetcode.com/problems/top-k-frequent-words/description/
 * tag: Hash Table, String, Trie, Sorting, Heap (Priority Queue), Bucket Sort, Counting
 */

class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        Map<String, Integer> map = new HashMap<>();
        for(String word: words){
            map.put(word, map.getOrDefault(word, 0) + 1);
        }

        List<String>[] helper = new ArrayList[words.length + 1];
        for(int i = 0; i < words.length + 1; i++){
            helper[i] = new ArrayList();
        }

        for(Map.Entry<String, Integer> entry: map.entrySet()){
            helper[entry.getValue()].add(entry.getKey());
        }

        List<String> result = new ArrayList();
        for(int i = helper.length - 1; i >= 0; i--){
            Collections.sort(helper[i]);
            for(String s: helper[i]){
                result.add(s);
                if(result.size() == k) {
                    return result;
                }
            }
        }
        return result;
    }
}