import java.util.*;

class groupAnagrams {
    public List<List<String>> groupAnagrams(String[] strs) {

        Map<String, List<String>> groupMap = new HashMap<>();

        for (String word : strs) {
            // Convert the word to a char array and sort it to create a key
            char[] chars = word.toCharArray();
            Arrays.sort(chars);
            String sorted = new String(chars);

            // Group the word using the sorted string as the key
            groupMap.computeIfAbsent(sorted, k -> new ArrayList<>()).add(word);
        }

        // Return only the grouped lists
        return new ArrayList<>(groupMap.values());
    }
}