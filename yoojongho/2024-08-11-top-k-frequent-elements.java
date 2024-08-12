/**
 * Leetcode
 * problem: 347
 * link: https://leetcode.com/problems/top-k-frequent-elements/description/
 * tag: Array, Hash Table, Divide and Conquer, Sorting, Heap (Priority Queue), Bucket Sort, Counting, Quickselect
 */

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        int nl = nums.length; // nl: nums length
        if(nl<=k) { return nums; }

        Map<Integer, Integer> map = new HashMap<>();
        for(int num : nums) {
            map.put(num, map.getOrDefault(num, 0)+1);
        }
        List<Integer>[] helper = new ArrayList[nums.length + 1];
        for (int i = 0; i <= nums.length; i++) {
            helper[i] = new ArrayList<>();
        }
        for(int key: map.keySet()){
            int value = map.get(key);
            helper[value].add(key);
        }
        int[] result = new int[k];
        int idx = 0;
        for(int i = helper.length - 1; i >= 0; i--){
            for(int num: helper[i]){
                result[idx++] = num;
                if(idx == k) return result;
            }
        }
        return new int[0];
    }
}