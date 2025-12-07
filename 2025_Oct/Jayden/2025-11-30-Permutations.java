class Solution {
    /**
        Time Complexity: O(n * n!)
        Space Complexity: O(n * n!)
            - Each permuatation has n integers and there are n! permutations
     */
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        backtrack(nums, new ArrayList<>(), result);
        return result;
    }

    private void backtrack(int[] nums, List<Integer> path, List<List<Integer>> result) {
        if (path.size() == nums.length) {

            // must create a new list becuase path will get deleted afterwards so result will only contains the empty lists at the end
            result.add(new ArrayList<>(path));
            return;
        }

        // try placing each number in current position
        for (int num : nums) {
            if (path.contains(num)) continue;

            path.add(num);

            // go further with this combination
            backtrack(nums, path, result);

            // backtrack so we can try another number
            path.remove(path.size() - 1);

        }
    }
}