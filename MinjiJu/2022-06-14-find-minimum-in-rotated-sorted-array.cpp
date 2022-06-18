// binary search O(log(n))
class Solution {
public:
    int findMin(vector<int>& nums) {
        int lo=0, hi=nums.size()-1;
        
        while(lo<hi){
            auto mid = lo + (hi-lo)/2;
            
            if(nums[mid]<nums[hi]) hi = mid;
            else if(nums[mid]>nums[hi]) lo = mid+1;
        }
        return nums[lo];
    }
};


class Solution {
public:
    int findMin(vector<int>& nums) {
        
        int left=0, right=nums.size()-1;        

        while(left < right){
            
            if(nums[left] < nums[right]) {
                return nums[left];
            }
            
            int mid = (left+right)/2;
            
            if(nums[left] > nums[mid]){
                right = mid;
            } else {
                left = mid+1;
            }
        }
        return nums[left];
    }
};


class Solution {
public:
    int findMin(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        return nums[0];
    }
};