class Solution {
    public int search(int[] nums, int target) {
        //ascending, distinct
        //target을 찾으면 거기서 rotate
        //target의 index를 return
        //time complexity -> not n, has to be log n
        int end = nums.length-1;
        int start = 0;

        while(start<=end) {
            int mid = (start + end) /2;
            if(nums[mid] == target) return mid;

            if(nums[mid] >= nums[start]) {
                if(target < nums[mid] && target >= nums[start]) {
                    end = mid -1;
                }else {
                    start = mid + 1;
                }
            }else {
                if(target>nums[mid] && target<=nums[end]) {
                    start = mid +1;
                }else {
                    end = mid -1;
                }
            }
        }
        
        return -1;
    }
}