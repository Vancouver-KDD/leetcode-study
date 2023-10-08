class Solution {
    public int[] searchRange(int[] nums, int target) {
        int tempArr[]  = new int [nums.length]; // temp array to store the index of target
        int result[] = new int[2];
        int index = 0;
        // edge case
         if (nums == null || nums.length == 0) {
            result[0] = -1;
            result[1] = -1;
            return result;
         }
       for (int i = 0; i < nums.length; i++) {
        // when target is found, store the index in temp array
           if (nums[i] == target) {
               tempArr[index++] = i;
           } else {
            // if target is not found, check if it is the last element in the array
               if (i == nums.length -1  && index == 0) {
                result[0] = -1;
                result[1] = -1;
                return result;
               }
           }
       }
       result[0] = tempArr[0];
       result[1] = tempArr[index-1]; // because index is incremented after storing the index of target
       return result;
    } 
}