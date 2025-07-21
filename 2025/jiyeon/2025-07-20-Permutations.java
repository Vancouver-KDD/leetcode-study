class Permutations {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> answer = new ArrayList<>();
        backtrack(nums, answer, new ArrayList<>());
        return answer;
    }

    private void backtrack(int[] nums, List<List<Integer>> answer, List<Integer> current) {
        if (current.size() == nums.length) {
            answer.add(new ArrayList<>(current));
            return;
        }

        for (int num : nums) {
            if (!current.contains(num)) {
                current.add(num);
                backtrack(nums, answer, current);
                current.remove(current.size() - 1);
            }
        }
    }
}