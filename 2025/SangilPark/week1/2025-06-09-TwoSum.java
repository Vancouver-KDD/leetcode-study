package week1;
import java.util.*;

/*
 * Week 1: Array & Hashing
 * https://leetcode.com/problems/two-sum/
 */
class Solution {
    public static int[] twoSum(int[] nums, int target) {
        // 1. brute force O(n^2)
        // 2. hash table O(n) : put differ into hashMap, check
        // key : value, value : index

        Map<Integer, Integer> idxMap = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++) {
            int differ = target-nums[i];
            if (idxMap.containsKey(differ)) {
                return new int[] {i, idxMap.get(differ)};
            }
            idxMap.put(nums[i], i);
        }
        
        return new int[2];
    }

    public static void main(String[] args) {
        int[] nums = {2,7,11,15};
        twoSum(nums, 9);
    }
}