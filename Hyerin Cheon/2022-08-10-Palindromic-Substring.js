function countSubstring(s){
  let count = 0;

  for(let i = 0; i < s.length; i++){
    // for odd length palindrome
    expand(s, i, i);
    // for even length palindrome
    expand(s, i - 1, i);
  }
  return count;

  function expand(s, left, right){
    while(s[left] && s[left] === s[right]){
      left--;
      right++;
      count++;
    }
  }
}