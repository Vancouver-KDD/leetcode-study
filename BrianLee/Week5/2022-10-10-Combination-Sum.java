class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        Arrays.sort(candidates);
        LinkedList<Integer> result = new LinkedList<>();
        List<List<Integer>> results = new ArrayList<>();
        helper(candidates, 0, target, result, results);
        return results;

    }

    public void helper(int[] candidates, int cur, int left, LinkedList<Integer> result, List<List<Integer>> results) {
        if(left == 0) {
            results.add(new ArrayList<>(result));
        }
        if(left < 0 ) return;

        for(int i = cur; i < candidates.length; i++) {
            int sum = candidates[i];
            int times = 0;
            while(sum <= left) {
                result.add(candidates[i]);
                times++;
                helper(candidates, i+1, left-sum, result, results);
                sum += candidates[i];
            }
            while(times-- > 0) {
                result.removeLast();
            }
        }
    }
}