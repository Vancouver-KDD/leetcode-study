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

// 1. 숫자별 등장 횟수 계산
        Map<Integer, Integer> numMap = new HashMap<>();
        for (int num : nums) {
            numMap.put(num, numMap.getOrDefault(num, 0) + 1);
        }

        // 2. bucket[i]에는 i번 등장한 숫자들이 들어감
        List<Integer>[] buckets = new List[nums.length + 1];
        for (int i = 0; i <= nums.length; i++) {
            buckets[i] = new ArrayList<>();
        }

        for (Map.Entry<Integer, Integer> entry : numMap.entrySet()) {
            int frequency = entry.getValue();
            int number = entry.getKey();
            buckets[frequency].add(number);
        }

        // 3. 뒤에서부터 순회하며 결과에 k개 담기
        List<Integer> result = new ArrayList<>();
        for (int i = buckets.length - 1; i >= 0 && result.size() < k; i--) {
            for (int num : buckets[i]) {
                result.add(num);
                if (result.size() == k) break;
            }
        }

        // 4. 결과 배열로 변환
        int[] resArr = new int[k];
        for (int i = 0; i < k; i++) {
            resArr[i] = result.get(i);
        }

        return resArr;
    }