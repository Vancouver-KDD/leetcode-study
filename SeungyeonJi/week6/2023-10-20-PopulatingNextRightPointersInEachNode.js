var connect = function (root) {
  if (!root) return null;
  const queue = [root];

  while (queue.length) {
    const size = queue.length;
    const level = { ...queue };

    for (let i = 0; i < size; i++) {
      const cur = queue.shift();
      cur.next = level[i + 1] ?? null;
      if (cur.left) queue.push(cur.left);
      if (cur.right) queue.push(cur.right);
    }
  }
  return root;
};
