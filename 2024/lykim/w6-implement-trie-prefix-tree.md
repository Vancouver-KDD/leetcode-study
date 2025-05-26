## Approach
- Initialize TrieNode representing a char by children, and boolean indicating if it's the end of the word or not. The children can utilize Hash, for the optimal search time complexity.
- The search function goes until the end of the word while the prefix search will stop before.

### Complexity
- Time complexity - O(W*L), while W is the number of words in the Trie and L is the average length of the words. 
- Space complexity - O(W*L)

### Solution
```
class TrieNode
    attr_accessor :children, :end_of_word
    def initialize()
        @children = Hash.new
        @end = false
    end
end

class Trie
    attr_accessor :root
    def initialize()
        @root = TrieNode.new
    end


=begin
    :type word: String
    :rtype: Void
=end
    def insert(word)
        cur = root

        for c in word.chars
            if !cur.children[c]
                cur.children[c] = TrieNode.new
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
        cur = root

        for c in word.chars
            return false if !cur.children[c]
            cur = cur.children[c]
        end

        return cur.end
    end


=begin
    :type prefix: String
    :rtype: Boolean
=end
    def starts_with(prefix)
        cur = root

        for c in prefix.chars
            return false if !cur.children[c]
            cur = cur.children[c]
        end

        true
    end
end

# Your Trie object will be instantiated and called as such:
# obj = Trie.new()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.starts_with(prefix)
```
