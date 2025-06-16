/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var characterReplacement = function(s, k) {
        const count = new Map()
        let result = 0
        let left = 0
        let maxFrequency = 0

        for(let right = 0; right < s.length; right++){
            count.set(s[right], (count.get(s[right]) || 0) + 1)
            maxFrequency = Math.max(maxFrequency, count.get(s[right]));
            while(right - left + 1 - maxFrequency > k){
                count.set(s[left], count.get(s[left]) - 1);
                left ++
            }
            result = Math.max(result, right - left + 1)
        }
        return result
};