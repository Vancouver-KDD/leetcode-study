class CombinationSum {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> answer = new ArrayList<>();
        backtrack(0, candidates, new ArrayList<>(), 0, target, answer);
        return answer;
    }

    private void backtrack(int index, int[] candidates, List<Integer> comb, int total, int target, List<List<Integer>> answer) {
        if (total == target) {
            answer.add(new ArrayList<>(comb));
            return;
        } else if (total > target || index == candidates.length) {
            return;
        }

        comb.add(candidates[index]);
        backtrack(index, candidates, comb, total + candidates[index], target, answer);
        comb.remove(comb.size() - 1);
        backtrack(index + 1, candidates, comb, total, target, answer);
    }
}
