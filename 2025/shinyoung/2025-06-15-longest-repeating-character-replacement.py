def characterReplacement(s: str, k: int) -> int:
    counts = {}
    max_count = 0
    left = 0
    result = 0
    for right in range(len(s)):
        c = s[right]
        counts[c] = counts.get(c, 0) + 1
        max_count = max(max_count, counts[c])
        window_size = right - left + 1
        if window_size - max_count > k:
            counts[s[left]] -= 1
            left += 1
        result = max(result, right - left + 1)
    return result

    

print(characterReplacement("ABAB", k=2))
print(characterReplacement("AABABBA", k=1))
print(characterReplacement("ABAA", k=0))
