import java.util.*;

class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        
        ArrayList<List<Integer>> result = new ArrayList<List<Integer>>();
        
        dfs(result, new ArrayList<Integer>(), candidates, target, 0 , 0 );
        
        return result;
    }
    
    
    private void dfs(ArrayList<List<Integer>>result, List<Integer> list, 
                     int[] candidates, int target, int sum, int start) {
        
       if(sum>target) {
           return;
       }
        if(sum==target){
            result.add(new ArrayList<>(list));
            return;
        }
        
        for(int i = start; i<candidates.length;i++) {
            list.add(candidates[i]);
            dfs(result, list, candidates, target, sum + candidates[i], i);
            list.remove(list.size()-1);
        }       
        
    }
    
    
}