public class Solution {
    public bool CanPartitionKSubsets(int[] nums, int k) {
        int sum = nums.ToList().Sum();
        Console.WriteLine(sum);
        if(sum%k != 0 ) return false;
        int target = sum/k;        
        return DoRecursion(k, 0, 0, nums, target);
    }
    public bool  DoRecursion(int curK, int curSum, int idx, int[] nums, int target){
        if(curK == 0) return true;
        for(int i = idx; i< nums.Length;i++ ){
            if(nums[i] != 0 && curSum + nums[i] <= target){
                int temp = nums[i];
                nums[i] =0;
                if(nums[i] != 0 && curSum + nums[i] == target){
    
                    if(DoRecursion(curK-1, 0, 0, nums, target)) return true;
                    nums[i] = temp;
                }else if(nums[i] != 0 && curSum + nums[i] < target){
                    int temp = nums[i];
                    nums[i] =0;
                    if(DoRecursion(curK, curSum+temp , idx+1, nums, target)) return true;
                
                }
                nums[i] = temp;
            }
            
        }        
        return false;
    }
}
