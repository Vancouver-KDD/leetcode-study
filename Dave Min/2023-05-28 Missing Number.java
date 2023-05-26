
class Solution {
    public int missingNumber(int[] nums) {
        boolean exist[] = new boolean[nums.length+1];
        for(var v : nums){
            exist[v] = true;
        }
        for(int i=0;i<exist.length;i++){
            if(!exist[i]) return i;
        }
        return 0;
    }
}
