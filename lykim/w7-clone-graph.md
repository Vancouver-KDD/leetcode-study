## Approach
- Starting from the given node, run depth first search of the neighbours to a copy. It's a connected graph so it will visit every node
- To skip copying the already visited node, maintain a hash `visited` to compare.

### Complexity
- Time complexity - O(E), when E is the number of edges. 
- Space complexity - O(n), when N is the number of vertices

### Solution
```
# Definition for a Node.
# class Node
#     attr_accessor :val, :neighbors
#     def initialize(val = 0, neighbors = nil)
#		  @val = val
#		  neighbors = [] if neighbors.nil?
#         @neighbors = neighbors
#     end
# end 

# @param {Node} node
# @return {Node}

def cloneGraph(node)
    @visited = Hash.new

    return nil if node.nil?
    return dfs(node) if node
    []
end

private def dfs(node)
    return @visited[node] if @visited[node]

    copy = Node.new(node.val)
    @visited[node] = copy
    for neighbor in node.neighbors do
        copy.neighbors.append(dfs(neighbor))
    end

    return copy
end
```
