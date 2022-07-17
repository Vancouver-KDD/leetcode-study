var cloneGraph = function(node){
  var map = {};
  return dfs(node);

  // for copy the graph node
  function dfs(n){
    // handle the null case
    if(!n) return null;
    // if we don't have the node in the map
    if(!map[n.val]){
      // copy the node and add it to the map
      map[n.val] = new Node(n.val);
      map[n.val].neighbors = n.neighbors.map(dfs);
    }
    return map[n.val];
  }
}