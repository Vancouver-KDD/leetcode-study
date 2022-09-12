//limitation:  if nums is null or size is zero, which return??
//input : [3, 2, 4], target: 6
//Time complexity: O(n), Space complexity: O(n)

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