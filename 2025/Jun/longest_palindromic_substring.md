
## Idea:

1. A palindrome has a center

2. Odd length example: "aba" → center is b

3. Even length example: "abba" → center is between the two bs

4. If you know the center, you can expand outward in both directions until the characters don’t match.

5. Do this for every possible center and track the longest one.

## Process:

1. Loop through each index in s

2. Treat it as an odd-length center and expand

3. Treat it as an even-length center and expand

4. Keep track of the longest palindrome found

⏱ Time complexity: O(n²) in worst case (we expand for each center)
📦 Space complexity: O(1) (we don’t store extra structures)

*When the loop ends, it’s because either left went too far left, or right went too far right, or s[left] != s[right].
That means the last valid palindrome was one step before the current left and right.

slicing is end-exclusive:
s[a:b]  # includes index a up to (but not including)
