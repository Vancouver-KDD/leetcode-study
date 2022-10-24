//2022.10.17
//Limitation : if nums is null or nums size is zero, return false
//Time Complexity: O(n) ???? 어떻게 계산하면될지 모르겠는데???
//Space Complexity: O(n) <- O(2n) :  First n originates from recursion. Second n comes from the usage of the memo table.
class Solution {
    
    
    public boolean canJump(int[] nums) {
        
        if(nums == null || nums.length == 0){
            return false;
        }
        
        Boolean[] isChecked = new Boolean[nums.length]; //default value is null
        
        return recursiveJump(nums, isChecked, 0);
        
    }
    
    private boolean recursiveJump(int[] nums, Boolean[] isChecked,  int pos){
        if(pos == (nums.length-1)){
            return true;
        }
        
        if(pos >= nums.length ){
            return false;
        }
           
        if(isChecked[pos] != null){ //already checked
           return isChecked[pos]; 
        }
           
        if(nums[pos] == 0){ //no more move
            isChecked[pos] = false;
            return false;
        }
        
        for(int i = 1; i <= nums[pos]; i++){
            if(recursiveJump(nums, isChecked, pos+i) == true){
                isChecked[pos] = true;
                return true;   
            }            
        }
        
        isChecked[pos] = false;
        return false;
    }
}