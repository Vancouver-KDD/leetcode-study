// A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
// Given a string s, return true if it is a palindrome, or false otherwise.

// Example 1:

// Input: s = "A man, a plan, a canal: Panama"
// Output: true
// Explanation: "amanaplanacanalpanama" is a palindrome.
// Example 2:

// Input: s = "race a car"
// Output: false
// Explanation: "raceacar" is not a palindrome.
// Example 3:

// Input: s = " "
// Output: true
// Explanation: s is an empty string "" after removing non-alphanumeric characters.
// Since an empty string reads the same forward and backward, it is a palindrome.

var isPalindrome = function(s) {
    s = s.toLowerCase().replace(/[\W_]/g, "");
     let left = 0;
     let right = s.length-1;
   
   while(left<right){
     if(s[left] === s[right]) {
       left ++;
       right--;
     }else{
        return false;
    }
   }
   return true;
 }

 //Time Complexity : O(logN) Just check half of the array
 //Space Complexity : O(1) No extra space needed
 