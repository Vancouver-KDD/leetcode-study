function levelOrder(root){
  if(!root) return [];
  let q = [root];
  let result = [];

  while(q.length){
    let row = [];
    let qlen = q.length;
    
    while(qlen > 0){
      let curr = q.shift();
      if(curr.left) q.push(curr.left);
      if(curr.right) q.push(curr.right);

      row.push(curr.val);
      qlen--;
    }
    result.push(row);
  }
  return result;
}