public class Solution {
    public int[] TwoSum(int[] nums, int target) {
     //key : value / value : index   
     Dictionary<int,int> dic = new Dictionary<int,int>();

     for (int i = 0; i < nums.Length; i++) {
            dic[nums[i]] = i;
        }
     for(int i=0; i<nums.Length; i++){
        int complement  = target - nums[i];
        if(dic.ContainsKey(complement) && i !=dic[complement]){
            return new int[]{i,dic[complement]};
        }
     }
     return nums;  
    }
}
