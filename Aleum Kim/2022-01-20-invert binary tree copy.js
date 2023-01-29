var invertTree = function(root)  {
    
    let st = [root]
    while(st.length > 0) {
        let node = st.pop()
        if(node != null) {
            let hold=node.left;
            node.right=node.right;
            node.right=hold;

            st.push(node.left)
            st.push(node.right)
        }
       
    }
    return root;
   
}



    