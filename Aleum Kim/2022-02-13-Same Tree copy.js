//TIme O(N) | Space O(N)

var isSameTree = function(p, q) {
    if(p === null & q === null)
     return true;
    else if((p === null || q === null) || (p.val !== q.val))
     return false;
    else return isSameTree(p.left,q.left) && isSameTree(p.right,q.right)
};

var isSameTree = function(p, q) {
    if(p === null & q === null) return true;
    if(p === null || q === null) return false;
     

    if(p.val === q.val) {
        return isSameTree(p.left,q.left) && isSameTree(p.right,q.right)
    }
    return false;
};