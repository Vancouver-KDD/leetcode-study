class Permute {
    public List<List<Integer>> permute(int[] nums) {
        
        List<List<Integer>> result = new ArrayList<>();
        backtracking(new ArrayList<>(), nums, new boolean[nums.length], result);
        return result;
    }

    public void backtracking(List<Integer> currentPermute, int[] nums, boolean[] used, List<List<Integer>> result){

        if (currentPermute.size() == nums.length){
            result.add(new ArrayList<>(currentPermute));
            return;
        }

        for(int i = 0; i<nums.length; i++){
            if (used[i])
                continue;

            currentPermute.add(nums[i]);
            used[i] = true;
            backtracking(currentPermute, nums, used, result);
            
            //backtracking
            currentPermute.remove(currentPermute.size() - 1);
            used[i] = false;
        }
    }
}