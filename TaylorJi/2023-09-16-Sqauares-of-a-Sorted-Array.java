package org.example;

import java.util.Arrays;

public class SortedSquares {
  //Brute Force, O(n^2), slow..
  public static int[] sortedSquares(int[] nums) {
    int[] sequared = new int [nums.length];
    int sequaredVal = 0;
    for (int i = 0; i < nums.length; i++){
      sequaredVal = (int)Math.pow(nums[i], 2);
      sequared[i] = sequaredVal;
    }
    Arrays.sort(sequared);
    return sequared;
  }


  public static void main(String[] args) {
    int[] result = sortedSquares(new int[]{-4,-1,0,3,10});
    System.out.println(Arrays.toString(result));
  }



}

