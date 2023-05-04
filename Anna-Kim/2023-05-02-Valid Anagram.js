//Given two strings s and t, return true if t is an anagram of s, and false otherwise.
//An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

// Input: s = "anagram", t = "nagaram"
// Output: true

// Input: s = "rat", t = "car"
// Output: false

// Hasmap in Javascript 

// Let s ='avcdaaf';
// Let arr = s.split('');
// Let map = {
// {} => key-value pairs
// [a,b,c,c,d,e,a] => {'a':2, 'b':1, 'c':2, 'd':1, 'e':1}

var isAnagram = function(s,t) {
    return (sorter(s) == sorter(t))
}
function sorter(str) {
    return str.split('').sort().join('')
}

// time complexity o(n) space complexity o(n)

var isAnagram = function (s, t) {
    if(s.length !== t.length) return false;

    let map = {}

    for(let i=0; i<s.length; i++) {
        let letter = s[i];

        if(!map[letter]){
            map[letter] = 1
        } else {
            map[letter]++
        }
    }

    for(let i=0; i<t.length; i++) {
        let letter = t[i];

        if(map[letter] == undefined){
            return false
        } if(map[letter] < 1) {
            return false
        }
            map[letter]--
        
    }
    return true;
};

// time complexity o(n+m) space complexity o(n)