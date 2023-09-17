package org.example;
import java.util.Arrays;

public class theeSumClosest {
  public static int threeSumClosest(int[] nums, int target) {
    Arrays.sort(nums);
    int closestSum = nums[0] + nums[1] + nums[2]; // Initialize closest sum with the sum of the first three elements

    for (int i = 0; i < nums.length - 2; i++) {
      // Two pointers, j move forward and k move backward
      int j = i + 1;
      int k = nums.length - 1;

      // avoid out of bound exception
      while (j < k) {
        int sum = nums[i] + nums[j] + nums[k];

        // if the sum is equal to the target, return immediately (closest possible sum)
        if (sum == target) {
          return target;
        }

        // if the sum is closer to target than the current closestSum, update closestSum to be sum
        if (Math.abs(target - sum) < Math.abs(target - closestSum)) {
          closestSum = sum;
        }

        // Move pointers based on the comparison with the target
        // if the sum is less than the target, it means we need a larger sum, so move j forward
        if (sum < target) {
          j++;
        } else {
          k--;
        }
      }
    }

    return closestSum;
  }



  public static void main(String[] args) {
    int result = threeSumClosest(new int[]{-1,2,1,-4}, 1);
    System.out.println(result);
  }
}