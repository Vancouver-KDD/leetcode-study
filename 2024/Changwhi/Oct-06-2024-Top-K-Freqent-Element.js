/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    
    const hashbox = {}
    const result = []

for(num of nums){
    if(!hashbox[num]){
        hashbox[num] = 0
    }
    hashbox[num] ++
}

    const sortedElements = Object.keys(hashbox)
        .sort((a, b) => hashbox[b] - hashbox[a]);
    return sortedElements.slice(0, k).map(Number);

};