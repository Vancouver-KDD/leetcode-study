
class Solution {
    public int[] productExceptSelf(int[] nums) {
        //O(1) extra space complexity
        //O(N) time complexity
        int len = nums.length;
        int [] answer = new int[len];
        //left to right
        answer[0] = 1;
        for(int i = 1; i<len;i++) {
            answer[i] = answer[i-1] * nums[i-1];
        }
        int acc = 1;
        for(int i = len-2;i>=0;i--) {
            acc *=nums[i+1];
            answer[i] = answer[i] * acc;
        }
        return answer;
    }
}