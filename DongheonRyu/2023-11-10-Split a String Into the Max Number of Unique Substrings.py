def maxUniqueSplit(s):
    def backtrack(start, substrings):
        if start == len(s):
            max_substrings[0] = max(max_substrings[0], len(substrings))
            return

        for i in range(start, len(s)):
            sub = s[start:i + 1]
            if sub not in seen:
                seen.add(sub)
                substrings.append(sub)
                backtrack(i + 1, substrings)
                substrings.pop()
                seen.remove(sub)

    max_substrings = [0]
    seen = set()
    backtrack(0, [])
    return max_substrings[0]