import java.util.*;

class Solution{
    public boolean validTree(int n, int[][] edges) {
        HashMap<Integer, ArrayList<Integer>> map = new HashMap<Integer, ArrayList<Integer>>();
        for(int i=0; i<n; i++){
            ArrayList<Integer> list = new ArrayList<Integer>();
            map.put(i, list);
        }
     
        for(int[] edge: edges){
            map.get(edge[0]).add(edge[1]);
            map.get(edge[1]).add(edge[0]);
        }
     
        boolean[] visited = new boolean[n];
     
        if(!helper(0, -1, map, visited))
            return false;
     
        for(boolean b: visited){
            if(!b)
                return false;
        }
     
        return true;
    }
     
    public boolean helper(int curr, int parent, 
                          HashMap<Integer, ArrayList<Integer>> map, boolean[] visited){
        if(visited[curr])
            return false;
     
        visited[curr] = true;
     
        for(int i: map.get(curr)){
            if(i!=parent && !helper(i, curr, map, visited)){
                return false;
            }
        }   
     
        return true;
    }
}