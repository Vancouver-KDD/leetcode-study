var cloneGraph = (node) => {
  if (!node) return node;

  let queue = [node],
    hash = {};
  hash[node.val] = new Node(node.val);

  while (queue.length) {
    const curr = queue.shift();
    curr.neighbors.forEach((n) => {
      if (hash[n.val] === undefined) {
        hash[n.val] = new Node(n.val);
        queue.push(n);
      }
      hash[curr.val].neighbors.push(hash[n.val]);
    });
  }
  return hash[node.val];
};
