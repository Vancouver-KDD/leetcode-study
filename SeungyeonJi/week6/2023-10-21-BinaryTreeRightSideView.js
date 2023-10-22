var rightSideView = function () {
  if (!root) return [];
  let queue = [root];
  let result = [];

  while (queue.length) {
    let size = queue.length;
    //push right size into result
    result.push(queue[queue.length - 1].val);

    while (size--) {
      let node = queue.shift();
      if (node.left) queue.push(node.left);
      if (node.right) queue.push(node.right);
    }
  }
  return result;
};
