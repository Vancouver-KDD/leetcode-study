
//2023-10-30
//Brute force - 아래 코드로 accepted 가 되긴 되네
//Time Complexity: O(n^2)
//Space Complexity: O(1)
/*
public class Solution {
    public int subarraySum(int[] nums, int k) {
        if(nums == null || nums.length <= 0){
            return 0;
        }
        
        int total = 0; 
        for(int i = 0; i < nums.length; i++){
            int sum = 0;
            for(int j = i; j < nums.length; j++){
                sum += nums[j];
                if(sum == k){
                    total++;
                }
            }
        }        
        return total;
    }
}
*/

//idea: Using HashMap<key, value> : key - sum, value - frequency(해당 sum 이 나타난 빈도수)  
//  nums의 각 요소를 더한 sum을 구했을때 Sum[i] - Sum[j] = k 라는 의미는 j+1 ~ i 까지의 subarray합이 K 라는 의미)) 를 이용.
//  => nums array 를 하나하나 체크하면서 sum 을 구하는데, 이때 매번 Sum 구하면서
//  sum -k 한 값이 map 에 있으면 그 frequency 만큼 totalCount 에 더하고, 
//  sum을 map 에 add, 이미 있으면 frequency 1증가해서 update 

//Time Complexity: O(N)
//Space Complexity: O(N)
public class Solution {
    public int subarraySum(int[] nums, int k) {
        if(nums == null || nums.length <= 0){
            return 0;
        }
        
        Map<Integer, Integer> sumMap = new HashMap<>(); //<key,value> = <sum, frequency>
        
        sumMap.put(0, 1); // 초기값 sum 이 0 인경우 1번, 을 꼭 넣고 시작해야함.
        // 그래야 nums=[1,1,1] ,k=2일때 [1,1] 의 경우 (sum -k = 2 -2 = 0) 체크 가능함.  
        int sum = 0;
        int totalNumber = 0;
        
        //nums:[1,1,1], k=2               nums:[-1,-1,0]  k=0
        //sum:0, 1,2, 3                   sum: 0, -1, -2, -2
        //prevSum: -1,0, 1                prevSum: -1, -2, -2
        //totalNum:0, 1, 2                totalNum: 0
        //map:(0,1) (1,1) (2,1) (3,1)     map: (0,1) (-1,1) (-2,1)
        for(int i = 0; i < nums.length; i++){
            sum += nums[i];
            int prevSum = sum - k;
            if(sumMap.containsKey(prevSum)){
                int frequency = sumMap.get(prevSum);
                totalNumber += frequency;
            }
            sumMap.put(sum, sumMap.getOrDefault(sum,0) + 1);
        }
        
        return totalNumber;
    }
}


//Limitation: nums is null or size is zero, return 0
//              if k is 0, return 0

//Input: nums = [1,1,1], k = 2   ---> Output: 2
//Input: nums = [1,2,3], k = 3   ---> Output: 2

//Leetcode Solution : 
//Time Complexity: O(N), Space Complexity: O(N)
/*
public class Solution {
    public int subarraySum(int[] nums, int k) {

        HashMap < Integer, Integer > sumMap = new HashMap < > ();
        sumMap.put(0, 1); // Sum 이 0 인 경우 (시작이 아무것도 선택안된경우 존재, 즉 [3, 1,2], k=3 일때 첫번째 값 1개가 k 와 같은경우 생김. )
        int prefixSum = 0;
        int answer = 0;
        
        for(int num : nums){
            prefixSum += num;
            answer += sumMap.getOrDefault(prefixSum -k, 0);
            sumMap.put(prefixSum, sumMap.getOrDefault(prefixSum, 0) +1);
        }
        return answer;
    }
}
*/

//Time Complexity: O(N^2), Space Complexity: O(1)
/*
class Solution {
    public int subarraySum(int[] nums, int k) {
        if(nums == null || nums.length == 0){
            return 0;
        }
        
        int count = 0; 
        
        for(int i = 0; i < nums.length; i++){
            int sum = 0;
            //int sum = nums[i];
            //if(sum == k){
            //    count++;
            //}
            //for(int j = i+1; j < nums.length; j++){
            for(int j = i; j < nums.length; j++){
                sum += nums[j];
                if(sum == k){
                    count++;
                }
            }
        }
        
        return count;
    }
}
*/