/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    const freqs = {};
    for (let num of nums) {
        if (freqs[num] === undefined) { 
            freqs[num] = 1; 
        } else {
            freqs[num] = freqs[num] + 1;
        }
    }
    
    const frequencyArray = [];
    for (let key in freqs) {
        frequencyArray.push([freqs[key], key]);
    }
    
    frequencyArray.sort((a, b) => {
        return b[0] - a[0];
    });
    
    const mostFreq = [];
    for (let i = 0; i < k; i++) {
        mostFreq.push(frequencyArray[i][1]);
    }
    
    return mostFreq;
};