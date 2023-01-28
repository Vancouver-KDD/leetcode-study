// Given two strings s and t, return true if t is an anagram of s, and false otherwise.

// An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

// Example 1:

// Input: s = "anagram", t = "nagaram"
// Output: true
// Example 2:

// Input: s = "rat", t = "car"
// Output: false

var isAnagram = function(s,t) {
    return (sorter(s) == sorter(t))
}

function sorter(str){
    return str.split('').sort().join('')
}



var isAnagram = function (s, t) {
    if(s.length === t.length) {
        let sArray = s.split('');
        let tArray = t.split('');
        
        sArray.sort().join('');
        tArray.sort().join('');
        for(let i=0; i<s.length; i++){
            if(sArray[i] !== tArray[i]) {
                return false;
            }
        }
        return true;
    } else {
        return false;
    }
   };