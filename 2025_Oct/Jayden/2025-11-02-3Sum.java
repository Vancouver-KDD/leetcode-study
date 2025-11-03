class Solution {
    public List<List<Integer>> threeSum(int[] nums) {

        /**
            Time complexity: O(n^2)
            Space complexity: O(1) or O(k) where k is nuber of triplets
         */
        Arrays.sort(nums);

        List<List<Integer>> result = new ArrayList<>();

        for (int pivot = 0; pivot < nums.length - 2; pivot++) {

            // skip duplicates
            if (pivot > 0 && nums[pivot] == nums[pivot - 1])
                continue;

            int left = pivot + 1;
            int right = nums.length - 1;

            while (left < right) {
                int sum = nums[pivot] + nums[left] + nums[right];

                if (sum == 0) {
                    result.add(Arrays.asList(nums[pivot], nums[left], nums[right]));

                    // skip duplicates
                    while (left < right && nums[left] == nums[left + 1]) left++;
                    while (left < right && nums[right] == nums[right - 1]) right--;

                    left++;
                    right--;

                // if sum is < 0 increase left pointer by 1 otherwise, decrease the right pointer
                } else if (sum < 0) {
                    left++;
                } else {
                    right--;
                }
            }

        }

        return result;
    }
}