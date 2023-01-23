import java.util.*;

class Solution {
    public int longestConsecutive(int[] nums) {
        //O(n) -> can't use sorting arrays
        int len = nums.length;
        int max= 0;
        Set<Integer> set = new HashSet<>();
        for(int i = 0; i<len;i++) {
            set.add(nums[i]);
        }

        for(int i = 0;i<len;i++) {
            int count = 1;
            int num = nums[i];
            while(set.contains(--num)) {
                count++;
                set.remove(num);
            }
            num = nums[i];
            while(set.contains(++num)) {
                count++;
                set.remove(num);
            }

            max = Math.max(max, count);
        }
        return max;
        
    }
}

