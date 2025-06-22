## Approach
- Initialize a WordNode representing a char by children, and boolean indicating if it's the end of the word or not. The children can utilize Hash, for the optimal search time complexity.
- Each added word will generate a tree branch, sharing the same path for the same part.
- The search without a dot, goes until the end of the word match.
- A search with a dot requires backtracking, checking all branches until the match is found. Use depth first search recursively.

### Complexity
- Time complexity - O(W*L), while W is the number of words in the Trie and L is the average length of the words. 
- Space complexity - O(W*L)

### Solution
```
class WordNode
    attr_accessor :children, :end
    
    def initialize()
        @children = Hash.new
        @end = false
    end
end

class WordDictionary
    attr_accessor :word
    def initialize()
        @root = WordNode.new
    end

=begin
    :type word: String
    :rtype: Void
=end
    def add_word(word)
        cur = @root

        for c in word.chars
            if !cur.children[c]
                cur.children[c] = WordNode.new
            end

            cur = cur.children[c]
        end

        cur.end = true
    end


=begin
    :type word: String
    :rtype: Boolean
=end
    def search(word)
        @word = word
        dfs(0, @root)
    end

    private def dfs(j, root)
        cur = root

        for i in j..(@word.size - 1)
            c = @word[i]
            
            if c != "."
                return false if !cur.children[c]
                cur = cur.children[c]
            else                                     # if it's a dot, it needs to search every child branch, until found - backtracking
                for child in cur.children.values
                    return true if dfs(i + 1, child)
                end
                return false    
            end
        end

        cur.end
    end
end
```
