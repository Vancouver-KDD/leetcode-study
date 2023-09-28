class Solution:
    '''
    Version 1.
    Using standard sliding windows template, find at most k false.
    
    template (which works for a lot of window problems)
    
    ---------------
    lo, hi = 0, 0
    while hi < len(input):
       do something (usually if statement)
       right += 1

       do something (usually either if or while statement)
       left += 1
    -----------------
    
    - If not enough falses, then expand window, and keep track of max
    - otherwise, shrink window.
    - since it can be longest T or F, we run search twice
    - eg) In another word, question can be understood as:
       1. find longest True sequence in T F T T 
       2. find logest True sequence in F T F F 
       3. find max of (point1, point2)
    runtime: O(n)
    space: O(1) # window has only 2 entries
    '''
    def maxConsecutiveAnswersV1(self, answerKey: str, k: int) -> int:

        def search(search_true):

            max_size = 0
            true_char, false_char = 'T', 'F'

            if not search_true:
                true_char, false_char = false_char, true_char

            left, right = 0, 0
            window = defaultdict(int)

            num_k = 0

            while right < len(answerKey):
                right_char = answerKey[right]
                window[right_char] += 1

                if right_char == false_char:
                    num_k += 1

                if num_k <= k:
                    max_size = max(max_size, right - left + 1)

                right += 1

                while num_k > k:
                    left_char = answerKey[left]
                    window[left_char] -= 1

                    if left_char == false_char:
                        num_k -= 1
                    left += 1

            return max_size

        true_search = search(True)
        false_search = search(False)

        return max(true_search, false_search)

    '''
    Version 2
    we calculate which has less numbers, T or F
    we can always "use" up the lesser one and convert it into majority (at most k)
    
    runtime: O(n)
    space: O(1)
    This runtime is same for V1 and V2, but current version is more readable, 
    and it does not require re-running sample input twice like v1. 
    '''
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:

        max_size = 0
        window = defaultdict(int)

        right = 0

        while right < len(answerKey):
            right_char = answerKey[right]
            window[right_char] += 1

            less_value = min(window['T'], window['F'])

            if less_value <= k:
                max_size += 1
            else:
                '''
                let say
                k = 2
                T F T F T T T (F) 
                               ^ 
                            right ptr

                in this else block:
                max_size = 7

                right =  7 (index)
                right - max_size  will point to the left pointer
                Then based on less_value, we will either shrink or expand 
                window
                '''
                left = right - max_size
                left_char = answerKey[left]
                window[left_char] -= 1

            right += 1
        return max_size