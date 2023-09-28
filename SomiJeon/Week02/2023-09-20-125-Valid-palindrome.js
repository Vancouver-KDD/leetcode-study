// A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

//todo: Given a string s, return true if it is a palindrome, or false otherwise.

//* Example 1:

// Input: s = "A man, a plan, a canal: Panama"
// Output: true
// Explanation: "amanaplanacanalpanama" is a palindrome.

//* Example 2:

// Input: s = "race a car"
// Output: false
// Explanation: "raceacar" is not a palindrome.

//* Example 3:

// Input: s = " "
// Output: true
// Explanation: s is an empty string "" after removing non-alphanumeric characters.
// Since an empty string reads the same forward and backward, it is a palindrome.

var isPalindrome = function (s) {
  // Remove non-alphanumeric characters and convert to lowercase
  const characterOnly = s.replace(/[^0-9a-z]/gi, "").toLowerCase();

  if (characterOnly.length < 2) {
    return true; // An empty string or a single character string is a palindrome
  }

  // Initialize pointers
  let left = 0;
  let right = characterOnly.length - 1;

  while (left < right) {
    if (characterOnly[left] !== characterOnly[right]) {
      return false; // If characters don't match, it's not a palindrome
    }

    left++;
    right--;
  }

  return true;
};
