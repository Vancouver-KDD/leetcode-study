class Solution {
    /**
        The depth of recursion depends on target and value sizes, not only on n.

        Let:
            N = length of candidates array
            T = target value
            M = minimum value among candidates

        Time Complexity: O(N * (T/M))
        Space Complexity: O(T/M)
     */
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<>();
        backtrack(candidates, target, 0, 0, new ArrayList<>(), result);
        return result;
    }

    private void backtrack(int[] candidates, int target, int startingIndex, int sum,
                           List<Integer> combination, List<List<Integer>> result) {

        // if current sum is equal to the target, add the combination in the result list and return the function call
        if (sum == target) {
            result.add(new ArrayList<>(combination));
            return;
        }

        // if the current sum is greater than the target, it means it's not a valid combination so return the function call
        if (sum > target) {
            return;
        }

        // start from the given index from the function call to find another candidate to form the combination
        for (int i = startingIndex; i < candidates.length; i++) {
            int candidate = candidates[i];
            combination.add(candidate);

            // since using the same element multiple times is allowed, try using the element at current index and pass the updated sum
            backtrack(candidates, target, i, sum + candidate, combination, result);

            // backtrack so we could try another number with current combination
            combination.remove(combination.size() - 1);
        }
    }
}
