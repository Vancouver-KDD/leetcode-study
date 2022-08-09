function isPalindrome(s){
  // turn string to lowercase and use regex to remove non-alphanumeric characters
  s = s.toLowerCase();
  s = s.replace(/[^A-Za-z0-9]/g, '');

  let leftIndex = 0;
  let rightIndex = s.length - 1;

  while(leftIndex < rightIndex){
    // palindrome needs to match the first and last one
    if(s[leftIndex] !== s[rightIndex]) return false;
    leftIndex++;
    rightIndex--;
  }
  return true;
}