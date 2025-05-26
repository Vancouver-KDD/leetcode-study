class Solution {
  /**
   * @param {number} n
   * @param {number[][]} edges
   * @returns {number}
   */
  countComponents(n, edges) {
    // 1. n means node number
    // 2. [a, b] means edge between a and b
    // 3. return number of connected components

    const adj = Array.from({ length: n }, () => []);
    const visit = Array(n).fill(false);

    for (const [u, v] of edges) {
      adj[u].push(v);
      adj[v].push(u);
    }

    const dfs = (node) => {
      for (const nei of adj[node]) {
        if (!visit[nei]) {
          visit[nei] = true;
          dfs(nei);
        }
      }
    };

    let res = 0;
    for (let node = 0; node < n; node++) {
      if (!visit[node]) {
        visit[node] = true;
        dfs(node);
        res++;
      }
    }
    return res;
  }
}
