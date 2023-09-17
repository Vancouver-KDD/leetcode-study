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


//    int threeNumbs = 3;
//    int gap;
//    int closeToTarget = 0;
//    if (nums.length == 3) {
//      return nums[0] + nums[1] + nums[2];
//    }
//
//    // the largest number index to fix
//    int holdIndex = nums.length - threeNumbs - 1;
//    HashMap<Integer, Integer> threeSumsResult = new HashMap<>();
//
//    for (int i = holdIndex; i < holdIndex + 1; i++) {
//      //adjust the for loop, this will cause outOfBound exception
//      for (int j = i + 1; j < nums.length - 1; j++) {
//        int temp3Sum = 0;
//        int[] threeNumbsArr = new int [threeNumbs];
//        threeNumbsArr[0] = nums[i];
//        threeNumbsArr[1] = nums[j];
//        threeNumbsArr[2] = nums[j+1];
//        temp3Sum = nums[i] + nums[j] + nums[j+1];
//        gap = Math.abs(Math.abs(temp3Sum) - Math.abs(target));
//        threeSumsResult.put(temp3Sum, gap);
//        //reset the 3numbsArr
//        threeNumbsArr = null;
//      }
//    }
//
//    int smallestGap = Collections.min(threeSumsResult.values());
//    for (int key : threeSumsResult.keySet()) {
//      if (threeSumsResult.get(key) == smallestGap) {
//        closeToTarget = key;
//      }
//    }
//
//    return closeToTarget;
  }



  public static void main(String[] args) {
    int result = threeSumClosest(new int[]{-1,2,1,-4}, 1);
    System.out.println(result);
  }
}