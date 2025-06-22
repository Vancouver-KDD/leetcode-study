class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # Store palindromes
        results = set()

        def helper(i, temp):
            if i >= len(s):
                results.add(tuple(temp))
                print(results)
            for right in range(i + 1, len(s) + 1):
                word = s[i:right]
                if word == word[::-1]:
                    # Check the next palindrome if the current one is found
                    temp.append(word)
                    helper(right, temp)
                    # backtrack
                    temp.pop()

        helper(0, [])
        return [list(t) for t in results]
