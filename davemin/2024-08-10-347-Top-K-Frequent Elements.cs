public class Solution {
    public int[] TopKFrequent(int[] nums, int k) {
                Dictionary<int,int> dic = new();
        foreach(var n in nums){
            if(!dic.ContainsKey(n)) dic.Add(n,1);
            else dic[n]++; 
        }
        return dic.OrderByDescending(kv => kv.Value).Take(k).Select(kv=>kv.Key).ToArray();
    }
}
