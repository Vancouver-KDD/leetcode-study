/**
 * // Definition for a Node.
 * function Node(val, left, right, next) {
 *    this.val = val === undefined ? null : val;
 *    this.left = left === undefined ? null : left;
 *    this.right = right === undefined ? null : right;
 *    this.next = next === undefined ? null : next;
 * };
 */

/**
 * @param {Node} root
 * @return {Node}
 */
var connect = function(root) {
    
    if(root == null){
        return null;
    }

    let q = new Queue();
    q.push(root);
    q.push(null);

    while(!q.isEmpty()){
        let front = q.front();
        q.pop();

        if(front == null){
            if(!q.isEmpty()){
                q.push(null);
            }
        }else{
            front.next = q.front();
            if(front.left){
                q.push(front.left);
                q.push(front.right);
            }
        }
    }

    return root;

};