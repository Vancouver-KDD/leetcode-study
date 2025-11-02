class Solution {

    public int[] topKFrequent(int[] nums, int k) {

        /*
            Time complexity: O(n)
            Space Complexity: O(n)
         */


        // Create HashMap to count number of encounters for unique elements
        Map<Integer, Integer> map = new HashMap<>();

        for (int num : nums) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }

        // Maximum frequency of a single number could have is the size of the original array
        List<Integer>[] bucketSortedArr = new ArrayList[nums.length + 1];
        for (int i = 0; i < bucketSortedArr.length; i++) {
            bucketSortedArr[i] = new ArrayList<>();
        }

        // Key : frequency of a unique number
        // Value: actual element
        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            bucketSortedArr[entry.getValue()].add(entry.getKey());
        }

        int[] result = new int[k];
        for (int i = bucketSortedArr.length - 1; k > 0; i--) {
            for (int j = 0; j < bucketSortedArr[i].size(); j++) {
                result[result.length - k] = bucketSortedArr[i].get(j);
                k--;
            }
        }

        return result;
    }
}