Skip to content
DEV Community 👩‍💻👨‍💻
Search...

Log in
Create account

0
Like
0
Jump to Comments
3
Save

codingpineapple
codingpineapple
Posted on Aug 28, 2021

LeetCode 417. Pacific Atlantic Water Flow (javascrpt solution)
#
javascript
#
algorithms
Description:
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

Solution:
Time Complexity : O(n^2)
Space Complexity: O(n^2)
var pacificAtlantic = function(heights) {
    // Set amount of rows and columns to variables
    const numRows = heights.length
    const numCols = heights[0].length

    // Create matrixes to hold which cells can visit each ocean
    const pacific = Array(numRows).fill().map(() => Array(numCols).fill(false))
    const atlantic = Array(numRows).fill().map(() => Array(numCols).fill(false))

    // Run dfs on first and last columns that touch an ocean
    for (let col=0 ;col<heights[0].length;col++){
       dfs(0, col, -Infinity, pacific)
       dfs(numRows - 1, col, -Infinity, atlantic)
    }

    // Run dfs on each cell on the top and bottom rows that touch an ocean
    for (let row = 0;row<heights.length; row++){
        dfs(row, 0, -Infinity, pacific)
        dfs(row, numCols - 1, -Infinity, atlantic)
    }

    // Starting from an edge of heights that touches an ocean, move inward and add all cells to the ocean matrix that can spill into the previously vistited cell
    function dfs(i, j, prev, ocean){
        // Stop dfs if we given coordinates that are not on the board, if the value of the cell we are visiting cannot spill water into the previous cell, or if we have already visited this cell
        if (i<0 || i >= numRows || j < 0 || j >= numCols || heights[i][j] < prev || ocean[i][j]) {
            return
        }

        // Set this cell as visited by the current ocean
        ocean[i][j] = true

        // Look in all directions to find more nodes that can visit the current ocean by flowing into the cell at [i, j]
        dfs(i+1, j, heights[i][j], ocean)
        dfs(i-1, j, heights[i][j], ocean)
        dfs(i, j+1, heights[i][j], ocean)
        dfs(i, j-1, heights[i][j], ocean)
    }

    const res = []

    // Check which cells [i, j] are able to touch both oceans by checking if a cell is in both ocean matrixes
    for (let i=0;i<numRows;i++){
        for (let j=0;j<numCols;j++){
            if (atlantic[i][j] && pacific[i][j]){
                res.push([i, j])
            }
        }
    }
    return res
}
Top comments (0)

Subscribe
pic
Add to the discussion
Code of Conduct • Report abuse
🌚 Browsing with dark mode makes you a better developer.
It's a scientific fact.

Read next
devsimc profile image
Re-posting For Better Reach : You are front-end developer? This is for you, Sample Data API
simc dev CSM® - Oct 12

mhdgmal1998 profile image
React Design Pattern -- Container Pattern
Mohammed Gamal Al-homaidi - Oct 15

smpnjn profile image
Javascript Shallow Copy - what is a Shallow Copy?
Johnny Simpson - Oct 22

anandprakash3 profile image
Top 7 Trending JavaScript Tools for Developers
Anand Prakash - Oct 10


codingpineapple
Follow
JOINED
Jun 27, 2020
More from codingpineapple
Leetcode 163. Missing Ranges (javascript solution)
#javascript #algorithms
LeetCode 1347. Minimum Number of Steps to Make Two Strings Anagram (javascript)
#algorithms #javascript
LeetCode 128. Longest Consecutive Sequence (javascript solution)
#algorithms #javascript
var pacificAtlantic = function(heights) {
    // Set amount of rows and columns to variables
    const numRows = heights.length
    const numCols = heights[0].length

    // Create matrixes to hold which cells can visit each ocean
    const pacific = Array(numRows).fill().map(() => Array(numCols).fill(false))
    const atlantic = Array(numRows).fill().map(() => Array(numCols).fill(false))

    // Run dfs on first and last columns that touch an ocean
    for (let col=0 ;col<heights[0].length;col++){
       dfs(0, col, -Infinity, pacific)
       dfs(numRows - 1, col, -Infinity, atlantic)
    }

    // Run dfs on each cell on the top and bottom rows that touch an ocean
    for (let row = 0;row<heights.length; row++){
        dfs(row, 0, -Infinity, pacific)
        dfs(row, numCols - 1, -Infinity, atlantic)
    }

    // Starting from an edge of heights that touches an ocean, move inward and add all cells to the ocean matrix that can spill into the previously vistited cell
    function dfs(i, j, prev, ocean){
        // Stop dfs if we given coordinates that are not on the board, if the value of the cell we are visiting cannot spill water into the previous cell, or if we have already visited this cell
        if (i<0 || i >= numRows || j < 0 || j >= numCols || heights[i][j] < prev || ocean[i][j]) {
            return
        }

        // Set this cell as visited by the current ocean
        ocean[i][j] = true

        // Look in all directions to find more nodes that can visit the current ocean by flowing into the cell at [i, j]
        dfs(i+1, j, heights[i][j], ocean)
        dfs(i-1, j, heights[i][j], ocean)
        dfs(i, j+1, heights[i][j], ocean)
        dfs(i, j-1, heights[i][j], ocean)
    }

    const res = []

    // Check which cells [i, j] are able to touch both oceans by checking if a cell is in both ocean matrixes
    for (let i=0;i<numRows;i++){
        for (let j=0;j<numCols;j++){
            if (atlantic[i][j] && pacific[i][j]){
                res.push([i, j])
            }
        }
    }
    return res
}
DEV Community 👩‍💻👨‍💻 — A constructive and inclusive social network for software developers. With you every step of your journey.

Built on Forem — the open source software that powers DEV and other inclusive communities.

Made with love and Ruby on Rails. DEV Community 👩‍💻👨‍💻 © 2016 - 2022.
