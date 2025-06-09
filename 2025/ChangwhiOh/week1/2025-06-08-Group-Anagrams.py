/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    /**
    1. use hashmap 
    2. convert each char in a string to unicode.
    3. in an array, there are 26 indices each slot contains 0
    4. index of unicode number increaments by 1
    5. use it as a key in an object(hashmap)
    6. if each word has the same array, push it to the key as a value
    7. reuturn values of a hashmap 
     */
    
    let hashmap = {}

    for (let word of strs){
        const count = new Array(26).fill(0);

        for (let i = 0; i < word.length; i++){
            count[word[i].charCodeAt(0) - 'a'.charCodeAt(0)] += 1
        }

        // convert into string to use it as a key
        const stringCount = JSON.stringify(count);
        if (!hashmap[stringCount]){
            hashmap[stringCount] = [];
        }
        hashmap[stringCount].push(word)
    }
    return Object.values(hashmap)

};