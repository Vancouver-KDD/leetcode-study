class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {

        /*
            Time Complexity: O(n * klog(k))
                - let k = length of words
                - takes O(k * log(k))) to sort chars
                - since operates to all words,
            Space Complexity: O(n)
         */

        // Key: word with sorted chars
        // Value: list of anagrams
        Map<String, List<String>> map = new HashMap<>();

        List<List<String>> result = new ArrayList<>();

        for (String str : strs) {

            // Sort chars and create it as new string for key
            char[] charArr = str.toCharArray();
            Arrays.sort(charArr);
            String sortedWord = new String(charArr);

            // Update or create list for the sorted key
            List<String> list = map.getOrDefault(sortedWord, new ArrayList<>());
            list.add(str);
            map.put(sortedWord, list);
        }

        result.addAll(map.values());

        return result;
    }
}