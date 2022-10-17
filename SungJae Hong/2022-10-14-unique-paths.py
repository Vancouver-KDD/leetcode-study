class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #start by putting bottom row to 1.
        row = [1] * n

        for i in range(m-1):
            newRow = [1] * n
            for j in range(n -2, -1, -1):
                newRow[j] = newRow[j +1] + row[j]
            #update the old row to new row.
            row = newRow
        return row[0]
# o (n +m)
# memory: o(n)
