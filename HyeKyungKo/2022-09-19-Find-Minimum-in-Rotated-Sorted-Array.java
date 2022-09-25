//2022-09-19
//Limitation: if nums is null or nums' size is 0, return -5001 ???? 
// Input: nums = [3,4,5,1,2] -> Output: 1
// Input: nums = [4,5,6,7,0,1,2] -> Output: 0
// Input: nums = [11,13,15,17] -> Output: 11

//Time Complexity: O(logn), Space Complexity: O(1)
class Solution{
    public int findMin(int[] nums){
        
        if(nums == null || nums.length == 0){
            return -50001;
        }
        
        if(nums.length == 1){
            return nums[0];
        }
        
        int start = 0; 
        int end = nums.length -1;
        
        
        while(start < end ){
            //it is ascending order array from start to end
            if(nums[start] < nums[end]){
                return nums[start];
            }
            
            int mid = (start + end) / 2;
            
            if(nums[start] <= nums[mid]){ 
                // from star to mid 는 오름차순, from mid+1 to end 에서 Rotated 됨.
                //It means nums[mid] > nums[end]
                //There is a minimum number between mid+1 and end
                start = mid+1;
            }else{ //nums[start] > nums[mid]
                //from start to mid 에서 Rotated 됨. 
                //There is a minimum number between start+1 and mid
                start = start+1;
                end = mid;
            }
            
        }
        
        //start == end
        return nums[start];
    }
}

//Time Complexity: O(logn), Space Complexity: O(logn), recursive call stack
/*
class Solution {
    public int findMin(int[] nums) {
        
        if(nums == null || nums.length == 0){
            return -5001;
        }
        
        return binarySearch(nums, 0, nums.length-1);
    }
    
    private int binarySearch(int[] nums, int start, int end){
        
        //it is the minimum number
        if(start >= end){
            return nums[start];
        }
        
        int mid = (start + end) / 2;
        
        
        if(nums[start] <= nums[mid]){
            
            //In case, ascending order from start to end
            if(nums[mid] < nums[end]){
                return nums[start]; 
            }else{
                //There is a minimum number between mid+1 and end
                return binarySearch(nums, mid+1, end); 
            }
        }else{ //nums[start] > nums[mid
            // there is a minimum number between start+1 and mid
            return binarySearch(nums, start+1, mid); 
        }        
        
    }
}
*/