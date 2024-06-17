public class Solution {
    public IList<IList<int>> ThreeSum(int[] nums) {
        // -1 -1 0 1 2 4
        IList<IList<int>> rval = new List<IList<int>>();
        Array.Sort(nums);
        //s: start pointer, l=left pointer, r=right pointer

        for(int s=0;s<nums.Length-2;s++){
            int l=s+1;            
            while(l<nums.Length-1){
                if( nums[s]+nums[l] >0) 
                    break;
                int r=nums.Length-1;    
                while(l<r){
                    if(nums[s] + nums[l] + nums[r] ==0){
                        rval.Add(new List<int>{nums[s] , nums[l] , nums[r]});
                    }
                    r--;
                }
                l++;
            }
        }
        return rval;
    }
}
