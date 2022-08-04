function characterReplacement(s, k){
  let start = 0;
  let end = 0;
  let maxFreq = 0;
  const visited = {};
  let result = 0;
  
  for(let end = 0; end < s.length; end++){
    const endChar = s.charAt(end);
    const startChar = s.charAt(start);
    
    visited[endChar] = visited[endChar] ? visited[endChar] + 1 : 1;
    
    maxFreq = Math.max(maxFreq, visited[endChar]);
    
    while(end - start + 1 - maxFreq > k){
      visited[startChar]--;
      start++;
    }
    result = Math.max(result, end - start + 1);
  }
  return result;
}