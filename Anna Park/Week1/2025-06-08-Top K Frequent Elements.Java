import java.util.*;

class topKFrequent {
    public int[] topKFrequent(int[] nums, int k) {
        
        Map<Integer, Integer> numMap = new HashMap<>();
        for (int num: nums){
            numMap.put(num, numMap.getOrDefault(num, 0) + 1);
        }

        PriorityQueue<Map.Entry<Integer, Integer>> maxHeap = new PriorityQueue<>((a, b) -> b.getValue() - a.getValue());

        for (Map.Entry<Integer, Integer> entry : numMap.entrySet()) {
            maxHeap.offer(entry);
        }

        int[] result = new int[k];
        for (int i = 0; i < k; i++) {
            result[i] = maxHeap.poll().getKey();
        }

        return result;
    }
}