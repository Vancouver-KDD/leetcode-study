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

var isPalindrome = function(str) {
    let arr = str.split('')
    let result =[]
    let alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'

    for(let i of arr) {
        if(alphabet.includes(i.toLowerCase())) {
            result.push(i.toLowerCase())
        }
    }
    return(result.join('') == result.reverse().join(''))
}

var isPalindrome = function(s) {
    s = s.toLowerCase()
    let start = 0 , end = s.length - 1
    
    const checkIfAlphaNumeric = (inputChar) => {
        if(((inputChar >= 'a') && (inputChar <= 'z')) || ((inputChar >= '0') && (inputChar <= '9'))) return true
        return false
    }
    while(start<end){
    if(s[start] === s[end]) {
         start++;
        end--;
        continue
    }
      
    if(!checkIfAlphaNumeric(s[start])) {
        start++;
        continue
    }
    if(!checkIfAlphaNumeric(s[end])) {
        end--;
        continue
    }
    return false
}
return true
};