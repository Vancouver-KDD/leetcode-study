var connect = function (root) {
  if (!root) return null;
  const queue = [root];

  while (queue.length) {
    const size = queue.length;
    //첫 루프때는 가장 위 level의 node만, 두 번째는 두 번째 level의 노드만 들어가게 된다
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
