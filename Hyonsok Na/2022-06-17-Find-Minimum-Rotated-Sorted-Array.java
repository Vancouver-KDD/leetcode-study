// couldn't solve
class Solution {
    public int findMin(int[] nums) {
        int r=nums.length/2;
        int l = r-1;
        int count=1;
        int output = 0;
        if(nums.length==1) return nums[0];
        if(nums[0]<nums[nums.length-1]) return nums[0];
        while(l<r) {
            if(nums[l]<nums[r]) {
                count++;
                r += nums.length/Math.pow(2,count);
                l = r-1;
            } else {
                output = nums[r];
                l=r+1;
            }
        }
        return output;
    }
}

//reference
class Solution {
    public int findMin(int[] nums) {
        int start=0,end=nums.length-1;
        int mid=0;
        if(nums[0]<=nums[end]){
            return nums[0];
        }
        while(start<=end){
            mid=start+(end-start)/2;
            if(mid < end && nums[mid]>nums[mid+1]) {
                return nums[mid+1];
            }
            if(mid>start && nums[mid-1]>nums[mid]){
                return nums[mid];
            }
            if(nums[start]<nums[mid]){
                start=mid+1;
            } else {
                end=mid-1;
            }
        }
        return -1;
    }
}