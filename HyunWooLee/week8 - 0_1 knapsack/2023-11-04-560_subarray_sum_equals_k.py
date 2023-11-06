def subarraySum(self, nums: List[int], k: int) -> int:
    dict = {0: 1}

    running_sum = 0
    result = 0
    for num in nums:
        running_sum += num

        if running_sum - k in dict:
            result += dict[running_sum - k]

        if running_sum not in dict:
            dict[running_sum] = 1
        else:
            dict[running_sum] += 1

    return result
