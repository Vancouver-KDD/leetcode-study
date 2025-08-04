import java.util.*;

class twoSum {
    public int[] twoSum(int[] nums, int target) {
        
        Map<Integer, Integer> numMap = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            // Calculate the number needed to reach the target
            int complement = target - nums[i]; 

            // If the complement already exists in the map, return the indices
            if (numMap.containsKey(complement)) {
                return new int[] { numMap.get(complement), i };
            }

            //store the current number with its index in the map
            numMap.put(nums[i], i);
        }

        // Return an empty array if no solution is found
        return new int[] {}; 
    }
}