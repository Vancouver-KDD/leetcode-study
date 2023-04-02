// You have a graph of n nodes.
// You are given an integer n and an array edges where edges[i] = [ai, bi]
// indicates that there is an edge between ai and bi in the graph.

// Return the number of connected components in the graph.

// Input: n = 5, edges = [[0,1],[1,2],[3,4]]
// Output: 2

// using DFS on each unvisited node in the graph keeping track of the number of connected components seen so far...
// time complexity is O(N + E): N is the number of nodes and E is the number of edges
// space complexity is O(N + E): the adjacency list to represent the graph and a boolean array to track visited nodes
class Solution {
    public int countComponents(int n, int[][] edges) {

        List<List<Integer>> adjList = new ArrayList<>();
        // boolean array to track visited nodes
        boolean[] visited = new boolean[n];
        int count = 0;
        
        // build adjacency list
        for (int i = 0; i < n; i++) {
            adjList.add(new ArrayList<>());
        }
        for (int[] edge : edges) {
            adjList.get(edge[0]).add(edge[1]);
            adjList.get(edge[1]).add(edge[0]);
        }
        
        // perform DFS on each unvisited node
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                dfs(i, adjList, visited);
                count++;
            }
        }
        
        return count;
    }
    
    private void dfs(int node, List<List<Integer>> adjList, boolean[] visited) {
        visited[node] = true;
        for (int adjNode : adjList.get(node)) {
            if (!visited[adjNode]) {
                dfs(adjNode, adjList, visited);
            }
        }
    }
}
