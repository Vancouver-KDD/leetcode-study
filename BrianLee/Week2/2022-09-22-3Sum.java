class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> results = new ArrayList<>();
        Arrays.sort(nums);

        int cur = 0;
        int pre = -1;
        while(cur < nums.length) {
            while(pre != -1 && cur < nums.length-2 && nums[pre] == nums[cur]) cur++;
            if(cur >= nums.length-2) break;
            pre = cur;
            int start = cur+1;
            int end = nums.length-1;
            while(start < end) {
                int sum = nums[cur] + nums[start] + nums[end];
                if(sum == 0) {
                    List<Integer> result = List.of(nums[cur], nums[start], nums[end]);
                    results.add(result);
                    end--;
                    start++;
                    while(end > 0 && nums[end] == nums[end+1]) end--;
                    while(start < nums.length && nums[start] == nums[start-1]) start++;
                } else if(sum > 0) {
                    end--;
                    while(end > 0 && nums[end] == nums[end+1]) end--;
                } else if(sum < 0) {
                    start++;
                    while(start < nums.length && nums[start] == nums[start-1]) start++;
                }
            }
        }
        return results;
    }
}