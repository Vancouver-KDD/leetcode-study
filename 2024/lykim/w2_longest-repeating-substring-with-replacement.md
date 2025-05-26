## Approach
- Set a sliding window and iterate the string, while moving window to the right and recording the frequency of chars by hash.
- If the length of the current sliding_window - max frequency is larger than the k variable, it means the left pointer needs to be moved to fill the gap. Otherwise keep moving to the next iteration.
- Find the longest size at each iteration then record

### Complexity
- Time complexity - O(n)
- Space complexity - O(n)

### Solution
```
# @param {String} s
# @param {Integer} k
# @return {Integer}
def character_replacement(s, k)
    char_counts = Hash.new(0)
    longest = 0

    left = 0
    max_f = 0

    chars = s.chars
    chars.each_with_index do |char, i|
        char_counts[char] += 1
        window_size = i - left + 1

        max_f = [max_f, char_counts[char]].max # Keep this for space optimiazation
        # if window_size - char_counts.values.max > k 
        if window_size - max_f > k 
            char_counts[chars[left]] -= 1
            left += 1 #only need to decrease length, then the condition will pass. No need while loop
        end

        longest = [longest, i - left + 1].max
    end

    longest
end
```

