## Approach
- Initialize TrieNode representing a char by children, and boolean indicating if it's the end of the word or not. The children can utilize Hash, for the optimal search time complexity.
- The search function goes until the end of the word while the prefix search will stop before.

### Complexity
- Time complexity - O(W*L), while W is the number of words in the Trie and L is the average length of the words. 
- Space complexity - O(W*L)

### Solution
```
# @param {Character[][]} board
# @param {String[]} words
# @return {String[]}
class TrieNode
    attr_accessor :children, :end
    def initialize()
        @children = Hash.new
        @end = false
    end

     def insert(word)
        cur = self

        for c in word.chars
            if !cur.children[c]
                cur.children[c] = TrieNode.new
            end
            cur = cur.children[c]
        end

        cur.end = true
    end
end


def find_words(board, words)
    root = TrieNode.new
    
    # Create a Trie with given word list
    for word in words
        root.insert(word)
    end

    @board = board
    @row_num = board.size
    @col_num = board[0].size

    @res, @visited = Set.new, Set.new

    # Loop by the board, not by each word to be more efficient
    for i in 0..(board.size - 1)
        for j in 0..(board[0].size - 1)
            dfs(root, "", i, j)
        end
    end

    return @res.to_a
end

private def dfs(node, word, row, col)
    if row < 0 || col < 0 || row == @row_num || col == @col_num || !node.children[@board[row][col]] || @visited.include?([row, col])
        return
    end

    @visited.add([row, col])
    node = node.children[@board[row][col]]
    word += @board[row][col]
    if node.end
        @res.add(word)
    end

    dfs(node, word, row + 1, col)
    dfs(node, word, row - 1, col)
    dfs(node, word, row, col + 1)
    dfs(node, word, row, col - 1)
    @visited.delete([row, col])
end
```
