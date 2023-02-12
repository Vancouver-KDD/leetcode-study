import java.util.*;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(nums);
        int len = nums.length;
        for(int i = 0; i<len-2;i++) {
            //remove duplicate
            if (i > 0 && nums[i] == nums[i - 1]) {            
                continue;
            }
            int left = -nums[i];
            int start = i+1;
            int last = len-1;
            while(start<last){
                int sum = nums[start] + nums[last];
                if(sum == left) {
                    List<Integer> list = new ArrayList<>();
                    list.add(nums[i]);
                    list.add(nums[start]);
                    list.add(nums[last]);
                    result.add(list);
                    start++;
                    last--;
                    //remove dulicates again
                    while(start<last && nums[start]==nums[start-1]) start++;
                    while(start<last && nums[last]==nums[last+1]) last--;
                }else if(sum>left) {
                    last--;
                }else {
                    start++;
                }
            }
        }
        return result;
    }
}