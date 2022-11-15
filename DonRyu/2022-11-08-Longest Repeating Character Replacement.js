var characterReplacement = function(s, k) {
    // Keep count of all the characters in the string
    const chars = {}
    // left pointer, character with the current max frequency, return value
    let left = 0, maxf = 0, output = 0
    for(let right = 0; right < s.length; right++) {
        const char = s[right]
        // Increment count of the current character
        chars[char] = 1 + (chars[char] || 0)
        // Update the character frequency
        maxf = Math.max(maxf, chars[char])
        // Shrink the window of characters we are looking at until we can have a window of all the same characters + k charcters to change
        while((right-left+1) - maxf > k) {
                chars[s[left]] -= 1
                left++
          }
        // Update the output if the current window is greater than our previous max window
        output = Math.max(output, right - left +1)
    }
    return output
};
