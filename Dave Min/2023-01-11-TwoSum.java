import java.util.*;
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Hashtable<Integer,Integer> hashtable = new Hashtable<Integer,Integer>(); 
        int num=-1;
        for(int i=0;i<nums.length;i++){
            num = nums[i];
            if(!hashtable.containsKey(num)) {
                hashtable.put(num,i);
            }    
        }
        int pair=0;
        for(int i=0;i<nums.length;i++){             
            num = nums[i];
            pair = target - num;
            if(hashtable.containsKey(pair) && i !=hashtable.get(pair)) 
            return new int[]{i,hashtable.get(pair)};
        }  
        return null;
    }
}