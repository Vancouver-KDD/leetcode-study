// You have a graph of n nodes labeled from 0 to n - 1.
// You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates 
// that there is an undirected edge between nodes ai and bi in the graph.

// Return true if the edges of the given graph make up a valid tree, and false otherwise.

// Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
// Output: true

// Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
// Output: false

// undirected edge? means that two nodes is bidirectional and can be traversed in either direction
// for the input given, n 5 means there is 5 nodes labeled from 0 to 4
// to be a valid tree? must be an undirected graph that is connected with no cycles;
// there is only one unique path to reach one node from another node

// 1. using a modified depth-first search
// first condition: graph does not have a cycle
// second, graph is connected
// hasCycle function checks if there is a cycle in the graph
// by recursively visiting all the nodes in the graph and keeping track of the visited nodes and their parent node
// main function checks if the graph is connected and has no cycles
public boolean validTree(int n, int[][] edges) {

    List<List<Integer>> graph = new ArrayList<>();
    for (int i = 0; i < n; i++) {
        graph.add(new ArrayList<>());
    }

    for (int[] edge : edges) {
        int u = edge[0];
        int v = edge[1];
        graph.get(u).add(v);
        graph.get(v).add(u);
    }

    // check if the graph is a valid tree
    boolean[] visited = new boolean[n];
    boolean hasCycle = hasCycle(graph, 0, -1, visited);
    if (hasCycle) {
        // graph has a cycle
        return false;
    }
    for (boolean v : visited) {
        if (!v) {
            // graph is not connected
            return false;
        }
    }
    return true;
}

private boolean hasCycle(List<List<Integer>> graph, int u, int parent, boolean[] visited) {
    visited[u] = true;
    for (int v : graph.get(u)) {
        if (v == parent) {
            // skip the parent node
            continue;
        }
        if (visited[v]) {
            // the edge (u, v) forms a cycle
            return true;
        }
        if (hasCycle(graph, v, u, visited)) {
            // there is a cycle in the subgraph rooted at v
            return true;
        }
    }
    return false;
}
