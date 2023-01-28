/**
 * Given an integer array nums and an integer k, 
 * return the k most frequent elements. You may return the answer in any order.
 */

// 1. Create a HashMap to store the frequency of each element in the array.
// 2. Iterate through the input array and for each element, increment its count in the HashMap.
// 3. Create a List of Entry objects from the HashMap and sort it based on the values in descending order.
// 4. Iterate through the first k elements of the sorted list and add them to a final int array.
// 5. Return the final int array.
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
	// create a hashmap to store the frequency of each element in the array
	Map<Integer, Integer> map = new HashMap<>();
	// iterate the array and for each element, increment its count and store to the hashmap
	for(int num: nums) {
	    map.put(num, map.getOrDefault(num, 0) + 1);
	}
	// create a list to sort it based on the values in descending order
	List<Map.Entry<Integer, Integer>> list = new ArrayList<>(map.entrySet())
	// note that we will return the most k elements frequency (descending)
	list.sort((a, b) -> b.getValue() - a.getValue());
	nt[] result = new int[k];
	for (int i = 0; i < k; i++) {
	    result[i] = list.get(i).getKey();
	}
	return result;
    }
}

/** 
 * about Map.Entry and entrySet() method
 * Map<String, Integer> map = new HashMap<>();
 * map.put("apple", 1);
 * map.put("banana", 2);
 * map.put("orange", 3);
 * Set<Map.Entry<String, Integer>> entries = map.entrySet();
 * for (Map.Entry<String, Integer> entry : entries) {
 * System.out.println("Key: " + entry.getKey() + ", Value: " + entry.getValue());
 * }
 */