
public class Solution {
    public long MaximumSubarraySum(int[] nums, int k) {
        Dictionary<int,int> dic = new Dictionary<int,int>();
        int l=0, r =0;
        long max=0 , sum=0;

        while(r < nums.Length){
           if(!dic.ContainsKey(nums[r]))
                dic.Add(nums[r],0);
            dic[nums[r]]++;
            sum += nums[r];

            while(dic.Keys.Count < (r-l+1) || dic.Keys.Count > k)
            {                    
                if(dic.ContainsKey(nums[l]))
                {
                    sum -= nums[l];
                    dic[nums[l]]--;
                    if(dic[nums[l]] == 0)
                        dic.Remove(nums[l]);
                    l++;
                }
            }

            if(dic.Keys.Count == (r-l+1) && k == dic.Keys.Count)
           {
               max = Math.Max(sum,max);  
           }
           r++;
        }
        return max;
    }


}
