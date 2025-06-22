## Approach
- First create an adjacency list depth-first search.
- Iterate each node from 0, run depth first search and its neighbours. DFS will stop at the new component then increment the counter
- To skip checking the already visited node, maintain a hash visited to compare.

### Complexity
- Time complexity - O(N + E)
- Space complexity - O(N + E)

### Solution
```
def countComponents(n:, edges:)
    # Create an adjacency list representing the graph
    graph = Hash.new
    for i in 0..(n-1)
      graph[i] = []
    end

    for edge in edges:
        graph[edge[0]] << edge[1]
        graph[edge[1]] << edge[0]
    end

    @visited = Set.new
    @count = 0

    for i in 0..(n-1)
        unless @visited.include?(i)
            dfs(i)
            count += 1
        end
    end

    count
end

private def dfs(node):
    @visited.add(node)
    for neighbor in graph[node]
        dfs(neighbor) unless @visited.include?(neighbor)
    end
end
```
