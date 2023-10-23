var rightSideView = function(root) {
    const levels = [];
    
    if (root === null) return levels;
    
    const queue = [root];
    
    while (queue.length > 0) {
      let size = queue.length;
      const level = [];
      
      while (size > 0) {
        const top = queue.shift();
        
        level.push(top.val);
        
        if (top.left) queue.push(top.left);
        if (top.right) queue.push(top.right);
        
        size -= 1;
      }
      
      levels.push(level);
    }
    
    return levels.map(level => level[level.length - 1]);
  };