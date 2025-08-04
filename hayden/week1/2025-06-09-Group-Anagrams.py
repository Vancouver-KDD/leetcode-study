from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #dictionary will group words that are anagrams of each other
        anagrams = defaultdict(list)

        for word in strs:

            # Sort the letters in the word to create a common key
            # For example, "tea" and "eat" both become "aet" when sorted
            word_sorted = "".join(sorted(word))

            # Add the original word to the list that matches the sorted key
            anagrams[word_sorted].append(word)

        # Return just the grouped anagrams (ignore the keys)
        return list(anagrams.values())
