
class Solution {
    public int singleNumber(int[] nums) {
        HashSet<Integer> hset = new HashSet<Integer>();

        for(int i=0;i<nums.length;i++){
            if(hset.contains(nums[i])) hset.remove(nums[i]);
            else hset.add(nums[i]);
        }
        for(int i : hset){
            return i;
        }
        return 0;
    }
}
