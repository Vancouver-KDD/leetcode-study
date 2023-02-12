/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    let res = 0;
    let left = 0, right = height.length-1;
 
   
   while(left < right) {
       
       const currentArea = Math.min(height[left], height[right]) * (right - left);
       res = Math.max(currentArea, res);
       
         if(height[left] < height[right]) left++;
         else right--;
   }
   
 
     return res;
 };
 

 
// Time Complexity: O(n)
// Space Complexity : O(1) no extra space is needed

