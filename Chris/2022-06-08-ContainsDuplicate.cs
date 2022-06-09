public class Solution {
    public bool ContainsDuplicate(int[] nums) {
        Dictionary<int, bool> numDict = new Dictionary<int, bool>();
        
        foreach(int num in nums)
        {
            if(numDict.ContainsKey(num))
            {
                return true;
            }
            
            numDict.Add(num, true);
            
        }
        
        return false;
    }
}