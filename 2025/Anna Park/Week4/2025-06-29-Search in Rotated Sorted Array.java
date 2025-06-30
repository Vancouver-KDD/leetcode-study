// First Solution
import java.util.*;

class Solution1 {
    public int search1(int[] nums, int target) {

        int[] sorted = new int[nums.length];
        int pivot = 0;

        for(int i=0; i<nums.length; i++){
            if (nums[i] < nums[pivot]) 
                pivot = i;
        }

        for (int i=0; i<nums.length; i++){
            sorted[i] = nums[(i+pivot)%nums.length];
        }

        int left = 0 , right = nums.length -1; 
        while (left<=right){
            int mid = (left + right)/2;
            if (target==sorted[mid])
                return mid+pivot;
            else if (target<=sorted[mid]){
                right = mid - 1;
            } else{
                left = mid + 1;
            }
        }

        return -1;
    }
}

//수정 후 코드
class Solution2 {
    public int search2(int[] nums, int target) {
        int left = 0, right = nums.length - 1;

        while (left <= right) {
            int mid = (left + right) / 2;

            if (nums[mid] == target)
                return mid;

            if (nums[left] <= nums[mid]) {
                if (nums[left] <= target && target < nums[mid])
                    right = mid - 1;
                else
                    left = mid + 1;

            } else {
                if (nums[mid] < target && target <= nums[right])
                    left = mid + 1;
                else
                    right = mid - 1;
            }
        }

        return -1;
    }
}


