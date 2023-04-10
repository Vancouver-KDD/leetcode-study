// Given an array of strings strs, group the anagrams together. You can return the answer in any order.
// An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

// Example 1:

// Input: strs = ["eat","tea","tan","ate","nat","bat"]
// Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
// Example 2:

// Input: strs = [""]
// Output: [[""]]
// Example 3:

// Input: strs = ["a"]
// Output: [["a"]]


var groupAnagrams = function(strs) {
    const grouped = {};
    
    for(let i=0; i<strs.length; i++) {
        const word = strs[i];
        const key = word.split('').sort().join('');

        if(!grouped[key]) {grouped[key] = [];}
        grouped[key].push(word);
    }

    return Object.values(grouped);
}

// Time Complexity : O(N) Only use one loop and they calculate one loop till strs.length
// Space Complexity : O(1) The extra space is not needed (Using Hashmap)