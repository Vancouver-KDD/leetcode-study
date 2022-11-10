
//2022.10.24
//Limitation : if nums is null or size is zero, return 0?

//input: nums = [100,4,200,1,3,2] -> output : 4
//input: nums = [0,3,7,2,5,8,4,6,0,1] -> output: 9

//Idea : Using HashSet (no sorting algorithm. )

//Time Complexity : O(n)
//Space Complexity: O(n)
class Solution {
    public int longestConsecutive(int[] nums) {
        
        if(nums == null || nums.length == 0){
            return 0;
        }
        
        //make HashSet to find some number with O(n) time complexity
        HashSet<Integer> numSet = new HashSet<>();
        for(int i = 0; i < nums.length; i++){
            numSet.add(nums[i]);
        }
        
        int longest = 1;
        //check the consecutive sequence
        for(int num : nums){

            if(!numSet.contains(num-1)){ //first number of some consecutive sequence
                int consecutive = 1;
                int next = num+1;
                while(numSet.contains(next)){
                    consecutive++;
                    next++;
                }
                
                longest = Math.max(consecutive, longest);
            }
        }
        
        return longest;
    }
}