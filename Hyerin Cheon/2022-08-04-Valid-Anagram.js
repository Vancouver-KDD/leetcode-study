function isAnagram(s, t){
  // exceptional condition
  if(s.length !== t.length) return false;

  let letters = {};

  for(let i = 0; i < s.length; i++){
    // create hashmap for each letter of both 
    letters[s[i]] = letters[s[i]] ? letters[s[i]] + 1 : 1;
    letters[t[i]] = letters[t[i]] ? letters[t[i]] - 1 : -1;
  }

  // chek for duplicates
  // if all letters are the same, will end up with 0
  for(let letter in letters){
    if(letters[letter] !== 0) return false;
  }

  return true;
}