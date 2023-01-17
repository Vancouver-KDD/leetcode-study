/**
 * Given an array of strings strs, group the anagrams together. 
 * You can return the answer in any order.
 */

// using hashmap to store sorted string as a key(eat => aet, tae => aet), and original string as values (eat, tae)
// time complexity is O(N * klogk) as we iterate through the array (O(N)) and
// sort each string Array.sort which takes O(klogk) - k is the length of the string
public List<List<String>> groupAnagrams(String[] strs) {
    	// Key will be sorted string and values will be lists of origin strings
	Map<String, List<String>> groupedAnagrams = new HashMap<>();
	for (String str : strs) {
    	// get the character array
		char[] charArr = str.toCharArray();
		// sort
		Arrays.sort(charArr);
		String sortedStr = String.valueOf(charArr);
		// check if the sortedString is already exists
		if (!groupedAnagrams.containsKey(sortedStr)) {
    			// put key and empty array list
			groupedAnagrams.put(sortedStr, new ArrayList<>());
		}
		groupedAnagrams.get(sortedStr).add(str);
	}
	// return a list of grouped anagrams
	return new ArrayList<>(groupedAnagrams.values())
}

