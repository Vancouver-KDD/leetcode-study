class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Phone Keypad
        phone_numbers = {
            '2': ["a", "b", "c"],
            '3': ["d", "e", "f"],
            '4': ["g", "h", "i"],
            '5': ["j", "k", "l"],
            '6': ["m", "n", "o"],
            '7': ["p", "q", "r", "s"],
            '8': ["t", "u", "v"],
            '9': ["w", "x", "y", "z"],
        }
        
        def helper(i, temp):
            # Based on the index of the digits,
            # keep track of the combinations in temp
            # and add the final combination to the results
            if i >= len(digits):
                if len(temp) > 0:
                    results.add("".join(temp))
                    print("results: ", results)
                return
            
            num = digits[i]
            possible_letter = phone_numbers[num]
            # Go through all combinations with backtracking
            for letter in possible_letter:
                temp.append(letter)
                helper(i + 1, temp)
                temp.pop()

            
        # Store combinations in results
        results = set()

        # Iterate through the digits
        helper(0, [])
        
        return list(results)
