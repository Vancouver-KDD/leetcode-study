/*
Formula: If a sorted array is shifted, if you take the middle, always one side will be sorted. Take the recursion according to that rule.

1- take the middle and compare with target, if matches return.
2- if middle is bigger than left side, it means left is sorted
2a- if [left] < target < [middle] then do recursion with left, middle - 1 (right)
2b- left side is sorted, but target not in here, search on right side middle + 1 (left), right
3- if middle is less than right side, it means right is sorted
3a- if [middle] < target < [right] then do recursion with middle + 1 (left), right
3b- right side is sorted, but target not in here, search on left side left, middle -1 (right)
*/
//2022-09-20
// limitation: if nums is null or size is zero, return -1?  yes
//              Is it right that all values of nums are unique? yes
// Input: nums = [4,5,6,7,0,1,2], target = 0  -> Output: 4
// Input: nums = [4,5,6,7,0,1,2], target = 3  -> Output: -1
// Input: nums = [1], target = 0  -> Output: -1
// Input: nums = [3,1], target = 1  -> Output: 1
// Input: nums = [3,1], target = 2  -> Output; -1

//Time Complexity : O(logn), Space Complexity: O(1)
class Solution{
    
    public int search(int[] nums, int target){
        
        if(nums == null || nums.length == 0){
            return -1;
        }  
        
        int start = 0;
        int end = nums.length -1; 

        //target = 3
        //Index: 0 1 2 3 4 5 6
        //Value: 4,5,6,7,0,1,2
        
        //s:0, e:6, m: 3 
        //s:4, e:6  m: 5
        //s:6  e:6  m: 6 
        //s:6, , e: 5
        while(start <= end){

            int mid = (start + end) /2;
            if(nums[mid] == target){
                return mid;
            }
            
            if(nums[start] <= nums[mid]){//first half array is sorted in ascending odrer
                if((nums[start] <= target) && (target < nums[mid])){
                    end = mid - 1;
                }else{
                    start = mid + 1; 
                }           
            }else{ // Second half array is sorted in ascending order
                if((nums[mid] < target)&&( target <= nums[end])){
                    start = mid+1;
                }else{
                    end = mid-1; 
                }
            }
            
        }
        
        return -1; // there is no target in this array.
    }
}


//Time Complexity : O(logn), Space Complexity: O(logn) <- recursive call stack (맞을까?)
/*
class Solution {
    public int search(int[] nums, int target) {
        
        if(nums == null || nums.length == 0){
            return -1;
        }
        
        return recursiveSearch(nums, 0, nums.length -1, target);        
    }
    
    private int recursiveSearch(int[] nums, int start, int end, int target){
     
        if(start >= end){
            if(nums[start] == target){
                return start;
            }else{
                return -1;
            }
        }
        
        int mid = (start + end) / 2;
        
        if(nums[mid] == target){
            return mid;
        }
        
        
        if(nums[start] <= nums[mid]){ //At least,  first half of array is sorted in ascending order
            if( (nums[start] <= target) && (target < nums[mid])){ 
                //Target is in the part of ascending order array.
                return recursiveSearch(nums, start, mid-1, target);
            }else{ 
                return recursiveSearch(nums, mid+1, end, target);
            }
        }else{//Send half of array is sorted in ascending order
            
            if((nums[mid] < target)&&( target <= nums[end])){
                //Target is in the part of ascending order array.
                return recursiveSearch(nums, mid+1, end, target); 
            }else{
                return recursiveSearch(nums, start, mid-1, target);
            }
        }        

    }
}

*/