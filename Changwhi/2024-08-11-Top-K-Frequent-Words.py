class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
                
        # loop thorugh nums
        # using dic to store value and frequency
        # print out the k most freqent elements

        value_frequency = {}  # store number and occurrence

        # The indices in this array correspond to the occurrences, 
        # while the values correspond to the numbers in the given array.
        frequent = [[] for i in range(len(words)+1)]  

        for i in range(len(words)):
            value_frequency[words[i]] = 1 + value_frequency.get(words[i], 0)
        for key, value in value_frequency.items():
            print("key {} value {}".format(key, value))
            frequent[value].append(key)

        result = []     
        for index in range(len(frequent) - 1, -1, -1):
            # Sort the words with the same frequency alphabetically
            frequent[index].sort()
            for word in frequent[index]:
                result.append(word)
                if len(result) == k:
                    return result
                    
