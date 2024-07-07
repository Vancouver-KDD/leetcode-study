/**
 * Leetcode
 * problem: 15
 * link: https://leetcode.com/problems/3sum/
 * tag: Two Pointers
 */

/**
 * Approach
 * 1. If the length of the given 'nums' array is less than 3, return an empty list
 * 2. Sort the array to distinguish between same value.
 *  2-1. Skip checking for zero-sum when the values are same.
 *  2-2. Skip checking for zero-sum when the values are same, and move the left pointer.
 * 3. If the sum value is greater than 0, move the right pointer.
 * 4. If the sum value is less than 0, move the left pointer.
 * 5. If the sum value is 0, add it to the result list, and move the left pointer.
 */
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        // #1
        if(nums.length < 3) return Collections.emptyList();
        List<List<Integer>> result = new ArrayList();
        // #2
        Arrays.sort(nums);

        for(int i = 0; i < nums.length - 2; i++){
            // #2-1
            if(i > 0 && nums[i] == nums[i - 1]) continue;

            int j = i + 1;
            int k = nums.length - 1;

            while(j < k){
                int sum = nums[i] + nums[j] + nums[k];

                // #3
                if(sum > 0){ k--; }
                // #4
                else if(sum < 0){ j++; }
                else {
                    // #5
                    result.add(Arrays.asList(nums[i], nums[j], nums[k]));
                    j++;

                    // #2-2
                    while(nums[j] == nums[j - 1] && j < k) j++;
                }
            }
        }
        return result;
    }
}

/**
 * Failed: Time Limit Exceeded
 */
//class Solution {
//    public List<List<Integer>> threeSum(int[] nums) {
//        if(nums.length < 3) return Collections.emptyList();
//        Arrays.sort(nums);
//
//        int n = nums.length;
//        Set<List<Integer>> result = new HashSet();
//        for(int i = 0; i < n - 2; i++){
//            for(int j = i + 1; j < n - 1; j++){
//                for(int k = j + 1; k < n; k++){
//                    if((nums[i] + nums[j] + nums[k]) == 0){
//                        List<Integer> li = Arrays.asList(nums[i],nums[j],nums[k]);
//                        li.sort(null);
//                        result.add(li);
//                    }
//                }
//            }
//        }
//        return result.stream().collect(Collectors.toList());
//    }
//}