
//2023-09-29
//Idea : Sliding window + HashMap<key: nums[i], value: i> + prefixSum array
//   There are 'start' and 'end' positions. Both of them are '0' initially.
//   Do following steps in for (int end=0; end < inputstring.length(); end++) loop
//      - If nums[i] is new value, 1)add it to HashMap. 2) add its value to Sum
//      - else if HashMap contains 'nums[i]' already, check its previous position. 
//             - if the prev position is bigger than or same as the start position, it means that 'nums[i]' is not unique value in current window. so move start position to (nums[i] value's previous position + 1) and calculate 'sum' with new start position.
//      - update key:nums[i]'s value in HashMap

//Time Complexity: O(N)
//Space Complexity: O(N) , HashMap size + prefixSum array = 2N => O(N)

class Solution {
    public int maximumUniqueSubarray(int[] nums) {
        if(nums == null || nums.length <= 0){
            return 0;
        }
        
        int[] prefixSum = new int[nums.length+1];
        Map<Integer, Integer> uniqueMap = new HashMap<>(); //<key, value> : <nums[i], i>
        int start = 0;
        int maxSum = 0;
        for(int end = 0; end < nums.length; end++){
            if(uniqueMap.containsKey(nums[end])){
                int duplicatePos = uniqueMap.get(nums[end]);
                if(start <= duplicatePos){
                    start = duplicatePos + 1; //update start position
                }
            }
            
            uniqueMap.put(nums[end], end);
            prefixSum[end+1] = prefixSum[end] + nums[end];
            maxSum = Math.max(maxSum, prefixSum[end+1] - prefixSum[start]);
        }
        
        return maxSum;
    }
}



//Idea : Sliding window + HashMap<key: nums[i], value: i> 
// To get 'sum' in each steps in for loops,
//  - From previous start position to updated start , take away each value from total sum
//Time Complexity: O(N)
//Space Complexity: O(N) , hashMap
/*
class Solution {
    public int maximumUniqueSubarray(int[] nums) {
        if(nums == null || nums.length <= 0){
            return 0;
        }
        
        Map<Integer, Integer> uniqueMap = new HashMap<>();
        int start = 0;
        int maxSum = 0;
        int currSum = 0;
        for(int end = 0; end < nums.length; end++){
            if(uniqueMap.containsKey(nums[end])){
                while(start <= uniqueMap.get(nums[end])){
                    currSum -= nums[start];
                    start++;
                }
            }
            uniqueMap.put(nums[end], end);
            currSum += nums[end];
            maxSum = Math.max(maxSum, currSum);
        }
        return maxSum;
    }
}
*/    

//Idea : Sliding window + HashSet<key: nums[i]>
//  이 문제는 sum 을 구해야 하는 문제라서 start position 을 옮겨야 하는경우 
//  start position 부터 하나씩 거슬러 올라오면서 값들을 빼야 한다. 
//  HashMap 을 사용하던, HashSet 을 사용하던 똑같이 start position 을 하나씩 옮겨야 하기때문에 
//  HashSet 이 더 나을수도 있는 셈. 
//  Sum 이 아니라 longest 를 구하는 경우에는 HashMap을 쓰면, 한번에 position 을 알수 있는데
//  HashSet 을 쓰면 start 를 하나씩 하나씩 옮기는것을 중복되는 value 를 만날때까지 하는게
//  불필요한 동작이 된다. 
/*
class Solution {
    public int maximumUniqueSubarray(int[] nums) {
        
        if(nums == null || nums.length <= 0){
            return 0;
        }
        
        Set<Integer> uniqueSet = new HashSet<>();
        int start = 0;
        int maxSum = 0;
        int currSum = 0;
        for(int end = 0; end < nums.length; end++){
            while(uniqueSet.contains(nums[end])){
                currSum -= nums[start];
                uniqueSet.remove(nums[start]);
                start++;                
            }
            uniqueSet.add(nums[end]);
            currSum += nums[end];
            maxSum = Math.max(maxSum,currSum);
        }
        return maxSum;
    }
}
*/


//2023-01-25
//Input: nums = [4,2,4,5,6]

//Time Complexity: O(N)
//Space Complexity: O(N)
//아래는 HashMap 을 사용했는데 HashSet 만 쓰고도 할수 있음 
//  
/*
class Solution {
    public int maximumUniqueSubarray(int[] nums) {
        if(nums == null || nums.length == 0){
            return 0;
        }

        HashMap<Integer, Integer> uniqueMap = new HashMap<>();
        int start = 0;
        int sum = 0;  
        int maxScore = 0; 
        //[5,2,1,2,5,2,1,2,5]
        //map:      (5,0),(2,1),(1,2), (2,3)
        //start:      0     0     0     2
        //sum:        5, 5+2=7, 7+1=8, 8-5-2=1
        //maxScore:
        for(int i = 0; i < nums.length; i++){
            
            //if(!uniqueMap.containsKey(nums[i])){
            //    uniqueMap.put(nums[i], i); //add new data
            //    sum += nums[i];
           // }else{
            //    int duplicatePos =  uniqueMap.get(nums[i]);
            //    while(start <= duplicatePos){
            //        sum -= nums[start];
            //        start++;
            //    }
            //    uniqueMap.put(nums[i], i); //update data
            //}
            
            if(uniqueMap.containsKey(nums[i])){
                int duplicatePos = uniqueMap.get(nums[i]);
                while(start <= duplicatePos){
                    sum -= nums[start]; //remove data 
                    start++;
                }
            }
            uniqueMap.put(nums[i],i); //if nums[i] is unique, it is added for the first time, if it is not unique, the map data will be updated.
            sum += nums[i];
            maxScore = Math.max(maxScore, sum);
        }
        return maxScore;
    }
}
*/

//HashSet 을 사용해서 푼 경우 
/*
class Solution {
    public int maximumUniqueSubarray(int[] nums) {
        if(nums == null || nums.length == 0){
            return 0;
        }

        HashSet<Integer> uniqueSet = new HashSet<>();
        int start = 0;
        int sum = 0;  
        int maxScore = 0; 
        //[5,2,1,2,5,2,1,2,5]
        //map:      (5,0),(2,1),(1,2), (2,3)
        //start:      0     0     0     2
        //sum:        5, 5+2=7, 7+1=8, 8-5-2=1
        //maxScore:
        for(int i = 0; i < nums.length; i++){
            
            while(uniqueSet.contains(nums[i])){
                uniqueSet.remove(nums[start]);
                sum -= nums[start];
                start++;
            }
            uniqueSet.add(nums[i]); //if nums[i] is unique, it is added for the first time, if it is not unique, the map data will be updated.
            sum += nums[i];
            maxScore = Math.max(maxScore, sum);
        }
        return maxScore;

    }
}
*/