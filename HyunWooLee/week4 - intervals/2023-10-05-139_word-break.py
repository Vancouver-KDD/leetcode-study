class Node:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Solution:
    '''
    Step 1.
    - need to find matching intervals that always contains all word

    1. list all intervals (start, end)
    2. start matching 1 by 1
    let word length = 20

    0--A----8        // if first element starts at 0, then mark index = 8 as True
       4--B----12    // for B to be valid, there must be index 3 that must be True, but there isn't
             9--c---19  // for C to be valid, there must be index 8 that must be True. We have one.


    runtime: O(n^3)
    space: O(n)
    '''
    def wordBreakV1(self, s: str, wordDict: List[str]) -> bool:

        word_set = set(wordDict)
        intervals = []

        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i: j +1] in word_set:
                    # create intervals
                    intervals.append((i, j))

        visited = [False] * len(s)
        for interval in intervals:
            start, end = interval

            # if start is 0, then end is always a possible part of answer
            if start == 0:
                visited[end] = True
            # if start is not 0, then the the previous index must be valid
            elif visited[start -1]:
                visited[end] = True

        return visited[-1]

    '''
    Step 2.
    code optimization. 
    
    - we can do this in a single pass, because we do not need to sort intervals, and we can always figure out whether
    each element is valid.
    runtime: O(n^3)
    space: O(n)
    '''
    def wordBreakV2(self, s: str, wordDict: List[str]) -> bool:

        word_set = set(wordDict)
        visited = [False] * len(s)

        for start in range(len(s)):
            for end in range(start, len(s)):
                if s[start:end+1] in word_set:
                    if start == 0 or visited[start -1]:
                        visited[end] = True

        return visited[-1]

    '''
    Step 3. 
    if s[start:end+1] in word_set:
    This is O(n) operation.
    
    Alternatively, we can use Trie to check substring, at the cost of constructing Trie of wordDict.
    Creating Trie costs O(k) where k is number of characters in the dictionary
    
    runtime: O(n^2 + k) 
    space: O(n + k)
    '''

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def add_children(word):
            curr = root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = Node()
                curr = curr.children[char]
            curr.is_word = True

        root = Node()
        for word in wordDict:
            add_children(word)

        dp = [False] * len(s)
        for start in range(len(s)):
            curr = root
            for end in range(start, len(s)):
                curr_char = s[end]
                if curr_char not in curr.children:
                    break
                curr = curr.children[curr_char]

                if curr.is_word and (start == 0 or dp[start - 1]):
                    dp[end] = True

        return dp[-1]