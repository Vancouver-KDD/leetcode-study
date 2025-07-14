package week1;
import java.util.*;

/*
 * Week 1: Array & Hashing
 * https://leetcode.com/problems/top-k-frequent-elements
 */
class Solution {
    public static int[] topKFrequent(int[] nums, int k) {
        // count elements in Map -> heap
        Map<Integer, Integer> countMap = new HashMap<>();

        for (int num : nums) {
            countMap.put(num, countMap.getOrDefault(num, 0) + 1);
        }

        PriorityQueue<Map.Entry<Integer, Integer>> pq = new PriorityQueue<>(
            (o1, o2) -> o2.getValue() - o1.getValue()
        );

        for (Map.Entry<Integer, Integer> entry : countMap.entrySet()) {
            pq.offer(entry);
        }

        int[] result = new int[k];
        for (int i = 0; i < k; i++) {
            result[i] = pq.poll().getKey();
        }

        return result;
    }

    public static void main(String[] args) {
        
    }
}