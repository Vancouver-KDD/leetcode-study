public class Solution {
    public bool ContainsDuplicate(int[] nums) {
        HashSet<int> hset = new HashSet<int>();
        foreach(var n in nums){
            if(hset.Contains(n)) return true;
            hset.Add(n);
        }
        return false;
    }
}
