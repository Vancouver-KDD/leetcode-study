## Approach
- Start from each surrounding rows and columns, separating pacific/atlantic water flow, maintaining the valid path as set in pacific, atlantic.
- In each cell, do DFS to compare if the surrounding cell has the correct value for water flow (larger than the previous one), if then proceed, otherwise stop.
- Finally pick the ones that exist in the both pacific/atlantic set

### Complexity
- Time complexity - O(m*n)
- Space complexity - O(2*m*n)

### Solution
```
# @param {Integer[][]} heights
# @return {Integer[][]}
def pacific_atlantic(heights)
    @heights = heights
    @rows = heights.size
    @cols = heights.first.size
    pacific, atlantic = Set.new, Set.new

    for column in 0..(@cols - 1)  do
        dfs(0, column, pacific, heights[0][column]) # start from the top row for pacific ocean
        dfs(@rows - 1, column, atlantic, heights[@rows - 1][column]) # start from the bottom for atlantic 
    end

    for row in 0..(@rows - 1) do
        dfs(row, 0, pacific, heights[row][0]) # start from the left column for pacific
        dfs(row, @cols - 1, atlantic, heights[row][@cols - 1]) # start from the right side for atlantic
    end

    res = []
    for row in 0..(@rows - 1) do
        for column in 0..(@cols - 1) do
            if pacific.include?([row, column]) && atlantic.include?([row, column])
                res << [row, column]
            end
        end
    end

    res

end

def dfs(row, column, visit, prevHeight)
    # if it's already checked or row/column is invalid or the value is smaller than the current height, then don't record and stop checking, just return
    if visit.include?([row, column]) || row < 0 || column < 0 || row == @rows || column == @cols || @heights[row][column] < prevHeight
        return
    end
    
    visit.add([row, column])
    dfs(row + 1, column, visit, @heights[row][column])
    dfs(row - 1, column, visit, @heights[row][column])
    dfs(row, column + 1, visit, @heights[row][column])
    dfs(row, column - 1, visit, @heights[row][column])
end
```
