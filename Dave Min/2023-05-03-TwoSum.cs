public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int,int> dic = new Dictionary<int,int>();
        //adding the each number and the position from the array nums to HashTable  
        //Then, HashTable has key(array nums' element) and value(array nums' position)
        //While collecting the array's value, it will check the difference from target subtracted by the nums' value.
        //If the difference exist in the current HashTable, then the case ends and the each position will be returned.
        
        //Let's say the two duplicated numbers A1 and A2 are the answer.
        //While collecting the array value, in the A1 case, it will just move to the HashTable because A2 does not appear yet. 
        //Then in the A2 case, the difference A1 will be found in the HashTable.
        for(int i=0;i<nums.Length;i++){
            int diff = target - nums[i];
            if(dic.ContainsKey(diff)){
                 return new int[2]{dic[diff], i};// return the positions of the value
            }
            if(!dic.ContainsKey(nums[i])){
                dic.Add(nums[i],i);
            }
        }
        return new int[2];
    }
}
// Time Complexity : O(N) 
// Space Complexity : O(N) 
