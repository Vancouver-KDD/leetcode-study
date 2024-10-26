## Approach
- First iterate the matrix checking if the target is in the range of each array
  - ruby flatten method can replace this process, but it adds space complexity of O(m*n) though
- If that's the case use binary search


### Complexity
- Time complexity - O(mlog(n))
- Space complexity - O(1)

### Solution
```
# @param {Integer[][]} matrix
# @param {Integer} target
# @return {Boolean}
def search_matrix(matrix, target)
    # flattened = matrix.flatten
    
    row_index = nil
    for i in 0..matrix.size - 1 do
        if target <= matrix[i].last && matrix[i].first <= target
            row_index = i
            break
        end
    end

    return false unless row_index

    binary_search(0, matrix[row_index].size - 1, matrix[row_index], target)
end

def binary_search(left, right, array, target)
    return false if left > right

    mid = (left + right) / 2

    if array[mid] == target
        return true
    elsif array[mid] > target
        return binary_search(left, mid - 1, array, target)
    else
        return binary_search(mid + 1, right, array, target)
    end

    return false
end
```
