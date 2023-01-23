public class Solution {
    public int[] ProductExceptSelf(int[] nums) {        
        int a = nums.Length;
        int[] leftProduct = new int[nums.Length];
        //   1 2 3 4
        //-> 1 1 2 6
        int[] rightProduct = new int[nums.Length]; 
        //  1  2 3 4
        // 24 12 4 1 <-
        //-----------
        // 24 12 8 6

        for(int i=0;i<nums.Length;i++){
            if(i==0){
                leftProduct[i]=1;
                rightProduct[nums.Length -1 -i]=1;
                continue;
            }
                leftProduct[i] = nums[i-1] * leftProduct[i-1];
                rightProduct[nums.Length -1 -i] = nums[nums.Length -i] * rightProduct[nums.Length -i];            
        }
        for(int i=0;i<nums.Length;i++){
            leftProduct[i]=leftProduct[i]*rightProduct[i];
        }
        return leftProduct;
    }
}