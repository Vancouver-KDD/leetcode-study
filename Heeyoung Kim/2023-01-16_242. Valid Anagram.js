// 242. Valid Anagram

// Given two strings s and t, return true if t is an anagram of s, and false otherwise.

// An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

// Example 1:

// Input: s = "anagram", t = "nagaram"
// Output: true
// Example 2:

// Input: s = "rat", t = "car"
// Output: false

    
var isAnagram = function(s, t) {
  
    if(s.length !== t.length || s.length == 0 || t.length == 0) return false;
    //exception
    
    let map = {};
    
    for(let i=0; i<=s.length; i++){
      map[s[i]] = map[s[i]]? map[s[i]]+1 : 1;
    } 
    
    for(let j=0; j<t.length; j++) {
      if(!map[t[j]]) return false
      else map[t[j]]--;
    }
    
      return true;
};

// Time Complexity : O(n) Two traversals are needed, so the time complexity is O(n) 
// Space Complexity : O(1) No extra space is needed. 