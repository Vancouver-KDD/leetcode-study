/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var maxLevelSum = function(root) {
    let res = [];
    recursive(root,0);

    let greatest;

    for(let i = 0; i < res.length; i++){
        if(!greatest && greatest != 0){
            greatest = i;
        }else{
            if(res[greatest] < res[i]){
                greatest = i;
            }
        }
    }

    return greatest +1;

    function recursive(n, index){
        if(!n){
            return;
        }
        if(res[index]){
            res[index] += n.val;
        }else{
            res[index] = n.val;
        }
        recursive(n.left,index+1);
        recursive(n.right, index+1);
    }
};