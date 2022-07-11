class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> output = new ArrayList();
        List<Integer> combination = new ArrayList();
        Arrays.sort(candidates);
        if(candidates == null || candidates.length == 0) {
            return output;
        }
        
        toFindCombinationsToTarget(output, combination, candidates, target, 0);
        return output;
    }
    
    private void toFindCombinationsToTarget(List<List<Integer>> output, List<Integer> combination, int[] candidates, int target, int startIndex) {
        if(target == 0) {
            output.add(new ArrayList(combination));
            return;
        }
        for(int i = startIndex; i<candidates.length; i++) {
            if(candidates[i]>target) {
                break;
            }
            combination.add(candidates[i]);
            toFindCombinationsToTarget(output, combination, candidates, target - candidates[i], i);
            combination.remove(combination.size()-1);
        }
    }
}