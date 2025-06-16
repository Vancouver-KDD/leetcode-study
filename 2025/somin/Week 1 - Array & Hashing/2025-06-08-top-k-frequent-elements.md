347. Top K Frequent Elements

## Problem
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
https://leetcode.com/problems/top-k-frequent-elements


## Solution

```java
import java.util.*;

class Solution {
    public int[] topKFrequent(int[] nums, int k) {

        HashMap<Integer, Integer> freqMap = new HashMap<>(); 
        for(int num: nums){
            freqMap.put(num, freqMap.getOrDefault(num,0)+1);
        }   
        PriorityQueue<int[]> minHeap = new PriorityQueue<>(
            (a,b) -> Integer.compare(a[0],b[0])
        );

        for(Map.Entry<Integer, Integer> freqEntry: freqMap.entrySet()){
            minHeap.offer(new int[]{freqEntry.getValue(), freqEntry.getKey()});
            if(minHeap.size()> k){
                minHeap.poll();
            }
        }
        
      int[] result = new int[k];
        for (int i = 0; i < k; i++) {
            result[i] = minHeap.poll()[1];
        }

        return result;
    }
}
```

⏱️ Total Time & Space Complexity

Time	O(n log k)
Space	O(n)

Where:
n: the length of the nums array.
k: the number of top frequent elements to return.

Why:
Time: Building freqMap takes O(n), and inserting into a size-k min-heap takes O(log k) per item → O(n log k) total.
Space: O(n) to store frequencies in the map and O(k) for the heap → O(n) total.

