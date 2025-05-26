/**
 * @param {string} 
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
  let left = 0
  let result = 0
  const check = new Set()
  
  for(let right = 0; right < s.length; right++){
      if(check.has(s[right])){
          while(check.has(s[right])){
              check.delete(s[left])
              left ++;
          }
      }
      check.add(s[right]);
      result = Math.max(result, right - left + 1)
  }
  return result

};