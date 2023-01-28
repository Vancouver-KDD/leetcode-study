
//input: nums =[2, 7, 11, 15] , target 9 -> output =[0, 1]
//input: nums = [3, 2], target 9 -> output= null ???

//2023-01-14
//[idea]
//HashMap<key, value>: key= target - nums[i], value = i
// for loop -> if hashmap.containsKey(nums[j]) -> return array(hashmap.get(nums[j]), j)

//Time Complexity: O(N)
//Space Complexity: O(N)
class Solution{
    public int[] twoSum(int[] nums, int target){
        if(nums == null || nums.length <= 1){
            return new int[0];
        }

        HashMap<Integer, Integer> twoSumMap = new HashMap<>();

        //Input: nums = [2,7,11,15], target = 9
        //[0]:2 -> (7, 0), [1]:7 -> return {0, 1}
        for(int i = 0; i < nums.length; i++){
            if(twoSumMap.containsKey(nums[i])){
                return new int[]{twoSumMap.get(nums[i]), i};
            }else{
                twoSumMap.put(target - nums[i], i);
            }
        }

        return new int[0];
    }
}


//2022-12-01
//input: nums =[2, 7, 11, 15] , target 9 -> output =[0, 1]
//input: nums = [3, 2], target 9 -> output= null ???
/* 
class Solution{
    public int[] twoSum(int[] nums, int target){
        
        if(nums == null || nums.length == 0){
            return null;
        }

        //key: target - nums[index], value: index
        HashMap<Integer, Integer> sumMap = new HashMap<>(); 
        for(int i = 0; i < nums.length; i++){
            if(sumMap.containsKey(nums[i])){
                int[] result = {i, sumMap.get(nums[i])};
                //int[] result = new int[]{i, sumMap.get(nums[i])}; // 이렇게 생성해도됨.
                return result;
            }else{
                sumMap.put(target -nums[i], i); 
            }
        }

        return null;
    }
}
*/

//2022-06-10
//limitation:  if nums is null or size is zero, which return??
//input : [3, 2, 4], target: 6
//Time complexity: O(n), Space complexity: O(n)
/*
class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        if(nums == null || nums.length == 0){
            return null;
        }
        
        HashMap<Integer,Integer> diffMap = new HashMap<Integer,Integer>(); //key: diff , value: index
        
        int size = nums.length; 
        for(int i = 0; i < size; i++){
            if(diffMap.containsKey(nums[i])){ //succeed finding the set 
                int index = diffMap.get(nums[i]);
                int[] twoNumbers = {index, i};
                return twoNumbers;
            }else{ //fail to find the set
                int diff = target - nums[i];
                diffMap.put(diff, i);
            }
        }
        
        return null; // cannot find the set of two numbers
        
    }       
}
*/
















/*
class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        if(nums == null || nums.length == 0){
            return null;
        }
        
        HashMap<Integer,Integer>  map = new HashMap<>();
        
        for(int i = 0; i < nums.length; i++ ){
            map.put(nums[i], i);
        }
        
        for(int i =0; i < nums.length; i++){
            
            int diff = target - nums[i];
            if(map.containsKey(diff)){
                if( map.get(diff) != i){
                   int[] result = {i, map.get(diff)};
                    return result;
                }
            }
        }
                
        return null;
        
        
    }
}
*/

/*
class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        if(nums == null || nums.length == 0){
            return null;
        }
        
        Map<Integer, Integer> map = new HashMap<>();
        
        for(int i = 0; i < nums.length; i++){
            map.put(nums[i], i);
        }
        
        for(int i = 0; i < nums.length; i++){
            int diff = target - nums[i];
            
            if(map.containsKey(diff)){
                int indexValue = map.get(diff);
                if( i != indexValue){ // they are different
                    return new int[]{i, indexValue};
                }
                
            }
        }
        
        return null;
    }
}
*/

/*class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        Map<Integer, Integer> map = new HashMap<>();
        
        for(int i = 0; i < nums.length; i++){
            map.put(nums[i], i);
        }
        
        for(int i = 0; i < nums.length; i++){
            int value = target - nums[i];
            if(map.containsKey(value) && (map.get(value) != i)){
                return new int[]{i, map.get(value)};
            }
        }
        
        return null;
    }
}*/