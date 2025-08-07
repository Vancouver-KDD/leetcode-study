class CombinationSum {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {

        List<List<Integer>> result = new ArrayList<>();
        backtracking(new ArrayList<>(), candidates, target, result, 0);
        return result;
    }

    public void backtracking(List<Integer> currentCandidate, int[] candidates, int target, List<List<Integer>> result, int startIndex){

        int sum = 0;
        for (int i=0; i<currentCandidate.size(); i++){
            sum += currentCandidate.get(i);
        }
        if (sum==target){
            result.add(new ArrayList<>(currentCandidate));
            return;
        }

        for(int i=startIndex; i<candidates.length; i++){
            if (sum > target)
                continue;
            currentCandidate.add(candidates[i]);
            backtracking(currentCandidate, candidates, target, result, i);

            currentCandidate.remove(currentCandidate.size() -1);
        }
    }
}