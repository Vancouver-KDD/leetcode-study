function groupAnagrams(strs: string[]): string[][] {
    let map = new Map <string, string[]>()

    for(let str of strs) {
        const word = str.split('').sort().join('')

        if (!map.has(word)) {
            map.set(word, [])
        }   
        map.get(word)!.push(str)
    }
    return Array.from(map.values())
};

/* Create hashmaps to store the results values.
    reason : hashmap is faster than array for finding key.
             can access to key directly. 

    [string, string[]]

    //find key(word) from the map 
        //if there is existing key, add word to value
        //if not, add [word, [str]] to map

*/