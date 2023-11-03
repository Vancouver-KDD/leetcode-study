def subarraySum(nums, k):
    count = 0
    sum_count = {0: 1}  # Initialize a dictionary with default value 0: 1
    
    total_sum = 0
    
    for num in nums:
        total_sum += num
        if total_sum - k in sum_count:
            count += sum_count[total_sum - k]
        
        if total_sum in sum_count:
            sum_count[total_sum] += 1
        else:
            sum_count[total_sum] = 1
    
    return count
