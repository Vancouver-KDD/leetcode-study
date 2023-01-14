import java.util.*;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        //1.정렬한 다음, target 찾기 -> nlogn
        //2.하나씩 다 더하면서 찾아보기
        //3. map으로 활용해보기
        HashMap<Integer, Integer> map = new HashMap<>();
        int len = nums.length;
        for(int i = 0;i<len;i++) {
            if(map.containsKey(nums[i])) {
                return new int[] {map.get(nums[i]), i};
            }else {
                map.put(target-nums[i], i);
            }
        }
        return new int[2];
    }
}