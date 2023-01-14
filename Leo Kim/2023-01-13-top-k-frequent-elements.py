class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frequency = Counter(nums)
        table = frequency.most_common()
        ans = []

        for key, value in table:
            if k <= 0:
                break

            k -= 1
            ans.append(key)

        return ans

    ## amortised O(n)...? freq = O(n) + for loop worst = O(n) = O(2n) = O(n)...?