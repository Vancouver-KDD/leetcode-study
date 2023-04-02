import java.util.*;



public class LC_2023_02_26_ConstructBinaryTreeFromPreorderAndInorderTraversal {
	Map<Integer,Integer> map;
    int index;
	public class TreeNode {
	      int val;
	      TreeNode left;
	      TreeNode right;
	      TreeNode() {}
	      TreeNode(int val) { this.val = val; }
	      TreeNode(int val, TreeNode left, TreeNode right) {
	          this.val = val;
	          this.left = left;
	          this.right = right;
	      }
	  }
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        index = 0 ;
        // 해쉬맵에 키밸류값 저장해서 나중에 루트 찾고나면, 오른쪽트리 왼쪽트리 구별하려고
        map = new HashMap<>();
	
        int size = inorder.length;
        for(int i = 0 ; i < size;i++){
            map.put(inorder[i],i);
        }
        //트리 전체값 리턴
        return helper(preorder,inorder,0,size-1); 

    }
    private TreeNode helper(int[] preorder, int[] inorder, int low , int high){	

            if(low>high) return null;
		
            //루트값 찾기위함인듯? 근데 왜 index’++’ 인지 모르겠삼            
            int var = preorder[index++];
        	//루트 찾아서 트리 생성
            TreeNode root = new TreeNode(var);

            //루트로 기준 찾기
            int cut = map.get(var);
            //왼쪽트리 생성
            root.left= helper(preorder,inorder,low,cut-1);
            //오른쪽트리 생성
            root.right = helper(preorder,inorder,cut+1,high);

            return root;   
        }



}
