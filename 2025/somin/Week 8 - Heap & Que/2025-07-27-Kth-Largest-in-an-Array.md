```

class Solution {
    public int findKthLargest(int[] nums, int k) {
        // We want the (k-1)-th index in zero-based "greater-first" ordering
        return quickSelect(nums, 0, nums.length - 1, k - 1);
    }
    
    private int quickSelect(int[] a, int lo, int hi, int targetIdx) {
        if (lo == hi) return a[lo];
        
        // Choose pivot as middle element
        int pivot = a[lo + (hi - lo) / 2];
        
        // Partition: elements > pivot to left, < pivot to right
        int left = lo, right = hi;
        while (left <= right) {
            while (left <= right && a[left] > pivot) left++;
            while (left <= right && a[right] < pivot) right--;
            if (left <= right) {
                swap(a, left, right);
                left++;
                right--;
            }
        }
        
        // Now 'right' is end of left partition, 'left' is start of right partition
        if (targetIdx <= right) {
            return quickSelect(a, lo, right, targetIdx);
        } else if (targetIdx >= left) {
            return quickSelect(a, left, hi, targetIdx);
        } else {
            // targetIdx is between right+1 and left-1, which are equal
            return a[right + 1];
        }
    }
    
    private void swap(int[] a, int i, int j) {
        int t = a[i]; a[i] = a[j]; a[j] = t;
    }
}


```
