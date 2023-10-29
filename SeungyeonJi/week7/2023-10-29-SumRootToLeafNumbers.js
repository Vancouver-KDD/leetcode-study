var sumNumbers = function (root) {
  if (!root) null;
  let result = [];

  function recur(root, curArr) {
    if (!root) null;
    let curPit = root;
    curArr.push(curPit.val);

    if (!root.left && !root.right) {
      let num = Number(curArr.join(""));
      result.push(num);
    }

    if (root.left) recur(root.left, curArr);
    if (root.right) recur(root.right, curArr);
    curArr.pop();
  }
  recur(root, []);
  let num = 0;
  for (let i = 0; i < result.length; i++) {
    num += result[i];
  }

  return num;
};
