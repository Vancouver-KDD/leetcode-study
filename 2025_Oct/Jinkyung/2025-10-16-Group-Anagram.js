/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    const groups = new Map()
    for(const str of strs){
        const key = str.split('').sort().join('')
        
        if(!groups.has(key)) groups.set(key,[]);
        groups.get(key).push(str)
    }
    return Array.from(groups.values())
};