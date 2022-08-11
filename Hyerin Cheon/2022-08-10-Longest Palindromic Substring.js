function longestPalindrome(s){
  let longest = '';

  for(let i = 0; i < s.length; i++){
    let odd = expandFromCenter(s, i, i);
    let even = expandFromCenter(s, i - 1, i);

    let currLongest = odd.length < even.length ? even : odd;
    if(currLongest.length > longest.length){
      longest = currLongest;
    }
  }
  return longest;
}

function expandFromCenter(s, left, right){
  // s[left] --> as long as we don't hit the null
  while(s[left] && s[left] === s[right]){
    // keep expanding
    left -= 1;
    right += 1;
  }
  // if two characters are not same or hit null, return those two
  return s.slice(left + 1, right);
}