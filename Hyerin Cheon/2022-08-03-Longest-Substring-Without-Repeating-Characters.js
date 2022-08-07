function lengthOfLongestSubstring(s){
  let start = 0;
  let end = 0;
  let max = 0;
  // using has set
  const seen = new Set();

  while(end < s.length){
    // if it is not in the hash set
    if(!seen.has(s.charAt(end))){
      // add it and move to the next char
      seen.add(s.charAt(end));
      end++;
      // comapare has set size and current max val
      max = Math.max(seen.size, max);
    } else{
      // if it's already in there, delete the start char
      seen.delete(s.charAt(start))
      // and move the start to the next char
      start++;
    }
  }
  return max;
}