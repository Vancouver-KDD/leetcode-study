const search = function(nums, target){
    let left = 0, right = nums.length - 1, mid = 0;

    while(left <= right) {
        mid = Math.floor((left + right) /2);

        if(nums[mid] == target) return mid;

        if(nums[left] <= nums[mid]) {
            if(nums[left] <= target && target < nums[mid]) right = mid-1;
            else left = mid+1;
        }else if(nums[right] >= nums[mid]) {
            if(nums[mid] < target && target <= nums[right]) left = mid+1;
            else right = mid-1;
        }
    }

    return -1;
 
}


//Time Complexity : O(log N) : With using two pointer, check half element in the while loop
//Space Complexity : O(1) : No extra space needed
