public class Solution {
    public int[] ProductExceptSelf(int[] nums) {
        int length = nums.Length;

        
        int[] prefixProducts = new int[length];
        int[] suffixProducts = new int[length];
        
        int[] productExcept = new int[length];
        
        int prefixProduct = 1;
        int suffixProduct = 1;
        
        prefixProducts[0] = prefixProduct;
        suffixProducts[length - 1] = suffixProduct;
        
        for(int i = 1; i < length; i++){
            
            prefixProduct *= nums[i-1];
            prefixProducts[i] = prefixProduct;
            
            suffixProduct *= nums[length - i];     
            suffixProducts[length-1-i] = suffixProduct;
                     
        }
        
        for(int i = 0; i < length; i++){
            productExcept[i] = prefixProducts[i] * suffixProducts[i]; 
        }
        
        return productExcept;
            
        // Time Compl. = O(n)
        // Space Compl. = O(n)       
    }
}