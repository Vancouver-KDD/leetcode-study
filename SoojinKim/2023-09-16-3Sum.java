class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        
        List<List<Integer>> answer = new ArrayList<List<Integer>>();

        Arrays.sort(nums);

        for(int i=0; i<nums.length-2; i++){
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            int j = i + 1;
            int k = nums.length - 1;

            while (j < k) {

                int sum = nums[i] + nums[j] + nums[k];

                if (sum == 0) {
                    answer.add(Arrays.asList(nums[i], nums[j], nums[k]));

                    while (j < k && nums[j] == nums[j + 1]) {
                        j++;
                    }
                    while (j < k && nums[k] == nums[k - 1]) {
                        k--;
                    }
                    j++;
                    k--;

                }else if (sum < 0) {
                    j++;
                } else {
                    k--;
                }
            }
        }

        return answer;

    }
}