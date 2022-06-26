public class Solution {
    public IList<IList<int>> ThreeSum(int[] nums) {
        
        
        
        int target;
        int length = nums.Length;
        
        List<IList<int>> rList = new List <IList<int>>();
        IList<int> validSet = new List<int>();
        
        
        Array.Sort(nums);
        
        Dictionary<int,int> numDict = new Dictionary<int,int>();
        
        for(int i=0; i<length; i++){
            
            if(i>0 && nums[i] == nums[i-1]){
             continue;   
            }
            
            if(nums[i]>0){
                break;
            }
                
            
            target = -nums[i];
            for(int j=i+1; j<length; j++){
                if(j>1 && nums[j] == nums[j-2] && i != j-2){
                     continue;   
                    }
                if(numDict.ContainsKey(target - nums[j])){
                    validSet.Add(nums[i]);
                    validSet.Add(nums[j]);
                    validSet.Add(target - nums[j]);
                        
                    rList.Add(validSet);
                    validSet = new List<int>();
                    numDict.Remove(nums[j]);
                    numDict.Remove(target - nums[j]);
                } 
                numDict[nums[j]] = 1;
                
            }
            numDict.Clear();
        }
        
        return rList;
    }
}