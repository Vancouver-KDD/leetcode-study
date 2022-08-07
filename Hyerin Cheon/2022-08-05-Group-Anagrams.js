// using hashmap
// split('').sort().join('') --> sortedStrs
// if hash doesn't have, hash[sortedStrs[i]] = [strs[i]
// if has, just push the strs[i] to [sortedStrs[i]]


function groupAnagrams(strs){
  // split each word and sort it in ascending order
  const sortedStrs = strs.map(word => word.split('').sort().join(''));
  const hash = {};

  for(let i = 0; i < strs.length; i++){
    if(!hash[sortedStrs[i]]){
      hash[sortedStrs[i]] = [strs[i]];
    } else{
      hash[sortedStrs[i]].push(strs[i]);
    }
  }
  return Object.values(hash);
}