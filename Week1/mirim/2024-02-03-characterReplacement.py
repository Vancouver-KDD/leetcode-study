from collections import defaultdict


def characterReplacement(s: str, k: int) -> int:
    l, maxCount = 0, 0
    frequency = defaultdict(int)

    for r in range(len(s)):
        frequency[s[r]] += 1
        # cells count between left and right - highest frequency
        cellsCount = r - l + 1
        if cellsCount - max(frequency.values()) <= k:
            maxCount = max(maxCount, cellsCount)
        else:
            frequency[s[l]] -= 1
            if not frequency[s[l]]:
                del frequency[s[l]]
            l += 1

    return maxCount


print(characterReplacement("ABAB", 2), 4)
print(characterReplacement("AABABBA", 1), 4)
print(characterReplacement("ABCCZC", 2), 5)
