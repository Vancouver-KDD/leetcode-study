
//input: [1, 1, 1, 2, 2, 3] , k=2  -> output: [1, 2]
//input: [1], k= 1 -> output [1]

//2023-01-15
//Time Complexity: O(NlogK) <--- nums 배열각 요소마다(N개) PriorityQueue 재구성 (logK) -> N*logK
//Space Complexity: O(N + K) <--- HashMap size (N) + PriorityQueue size(K)
class Solution{
    public int[] topKFrequent(int[] nums, int k){
        if(nums == null || nums.length == 0 || k < 1){
            return new int[0];
        }

        HashMap<Integer, Integer> frequentMap = new HashMap<>();

        for(int i = 0; i < nums.length; i++){
            frequentMap.put(nums[i], frequentMap.getOrDefault(nums[i], 0)+1);
        }

        //int[] : int[0]- element, int[1]- count 
        // min heap -> ascending order of count
        PriorityQueue<int[]> pq = new PriorityQueue<int[]>((a,b)->(a[1]-b[1]));
        for(int key: frequentMap.keySet()){
            pq.add(new int[]{key, frequentMap.get(key)});
            if(pq.size() > k){
                pq.poll(); //Retrieves and removes the head of this queue,
            }
        }

        int[] result = new int[k];
        int count = 0;
        while(pq.size() > 0){
            int[] element = pq.poll();
            result[count++] = element[0];
        }

        return result;
    }
}


//2022-12-04
//Time Complexity: O(N)
//Space Complexity: O(N + N + K) = O(N)
/*
class Solution{
    public int[] topKFrequent(int[] nums, int k){
        if(nums == null || nums.length == 0 || k <=0) {
            return null;
        }  

        //save frequent for numbers 
        HashMap<Integer, Integer> frequentMap = new HashMap<>();
        for(int i = 0; i < nums.length; i++){
            if(frequentMap.containsKey(nums[i])){
                frequentMap.put(nums[i], frequentMap.get(nums[i])+1);
            }else{
                frequentMap.put(nums[i], 1);
            }
        }

        //save the numbers following frequency ( index is frequency)
        List<Integer>[] buckets = new List[nums.length+1];
        for(int i = 0; i < buckets.length; i++){
            buckets[i] = new ArrayList<>();
        }
        for(int key: frequentMap.keySet()){
            buckets[frequentMap.get(key)].add(key);
        }
        //save the numbers in descending order of frequency, 
        List<Integer> topList = new ArrayList<>();
        for(int i = buckets.length -1; i >= 0; i--){
            for(int j = 0; j < buckets[i].size(); j++){ //for(int value: buckets[i]) 와 동일. 만약 buckets[i].size() 가 0 이면 수행이 안됨. 
                topList.add(buckets[i].get(j));
            }
        }
        
        //get value from 0 index to 'k-1' index
        int[] result = new int[k];
        for(int i = 0; i < k; i++){
            result[i] = topList.get(i);
        }

        return result;
    }
}
*/
//2022-12-04
//Time Complexity: O(NlogK)
//Space Complexity: O(N+K)  <-- HashMap size (N) + PriorityQueue size(K)
/*
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        
        if(nums == null || nums.length == 0 || k <=0) {
            return null;
        }

        //save frequent for numbers 
        HashMap<Integer, Integer> frequentMap = new HashMap<>();
        for(int i = 0; i < nums.length; i++){
            if(frequentMap.containsKey(nums[i])){
                frequentMap.put(nums[i], frequentMap.get(nums[i])+1);
            }else{
                frequentMap.put(nums[i], 1);
            }
        }

        //Make min heap to find Top K frequent Elements
        //int[0]: element,  int[1]:frequency
        PriorityQueue<int[]> heap = new PriorityQueue<int[]>((a, b) -> (a[1] - b[1]));

        for(int key : frequentMap.keySet()){
            heap.add(new int[]{key, frequentMap.get(key)}); 
            if(heap.size() > k){
                heap.remove(); //heap.poll()과 동일, 제일 위에 있는 값을 제거 
            }
        }

        int[] result = new int[k];
        for(int i = k-1; i >= 0; i--){
            result[i] = heap.remove()[0]; //heap.poll()과 동일
        }

        return result;
    }
}
*/
