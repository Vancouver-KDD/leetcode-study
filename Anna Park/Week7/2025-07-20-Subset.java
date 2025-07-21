class Subsets {
    public List<List<Integer>> subsets(int[] nums) {

        List<List<Integer>> result = new ArrayList<>();
        backtracking(0, nums, result, new ArrayList<>());
        return result;
    }

    public void backtracking(int startIndex, int[] nums, List<List<Integer>> result, List<Integer> currentSubset){

        result.add(new ArrayList<>(currentSubset));

        for(int i=startIndex; i<nums.length; i++){
            currentSubset.add(nums[i]);
            backtracking(i+1, nums, result, currentSubset);
            currentSubset.remove(currentSubset.size() -1);
        }
    }
}