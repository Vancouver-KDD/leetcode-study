public class Solution {
    public int Search(int[] nums, int target) {        
        //1. Recursive Binary Search
        return BSearch(nums, target, 0, nums.Length-1);

        //2. Built-in Binary Search
        //int result = nums.ToList().BinarySearch(target);
        //return  result>=0?result:-1;
    }
    public int BSearch(int[] nums, int target, int x, int y) {
        if(x>y) return -1;
        int mid = (y+x)/2;

        if(nums[mid] == target) return mid;
        else if(nums[mid] < target) return BSearch(nums, target, mid+1, y);
        else return BSearch(nums, target, x, mid-1);
    }
}


//1. Recursive Binary Search 
//Time complexity: O(log n);
//Space complexity: O(log n);

//2. Built-in Binary Search
//Time complexity: O(log n);
//Space complexity: O(1);
