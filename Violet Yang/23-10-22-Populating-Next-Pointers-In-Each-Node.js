let connect = function(root) {
    if (!root) return root;
    
    const queue = [[0, root]];
    
    while (queue.length) {
        const [curNodelev, currNode] = queue.shift();
        
        if (queue.length) {
            const [nextNodelev, nextNode] = queue.shift();
            currNode.next = curNodelev === nextNodelev ? nextNode : null;
            queue.unshift([nextNodelev, nextNode]);
        } else {
            currNode.next = null;
        }
        
        currNode.left && queue.push([curNodelev + 1, currNode.left]);
        currNode.right && queue.push([curNodelev + 1, currNode.right]);
    }
    
    return root;
};