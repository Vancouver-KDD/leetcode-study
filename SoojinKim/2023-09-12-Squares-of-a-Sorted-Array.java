import java.util.*;

class Solution {
    public int[] sortedSquares(int[] nums) {
        int numsLength = nums.length;
        int[] answer = new int[numsLength];
        
        int p1 = 0;
        int p2 = numsLength-1;
        for(int i=numsLength-1; i>=0; i--){
            if(Math.abs(nums[p1])>Math.abs(nums[p2])){
                answer[i]= nums[p1]*nums[p1];
                p1++;
            }else{
                answer[i]= nums[p2]*nums[p2];
                p2--;
            }
        }

        return answer;
    }
}