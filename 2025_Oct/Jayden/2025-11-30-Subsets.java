class Solution {
    /**
        Time Complexity: O(N * 2^N)
            - For every subSets, creating new list takes O(n)
        Space Complexity: O(N * 2^N)
            - For each subSet creation, copying n up to n elements
     */
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();

        // starts with an empty set
        result.add(new ArrayList<>());

        for (int num : nums) {
            int size = result.size();

            // for all the subsets already created, new element should be added and becomes a new subset
            for (int i = 0; i < size; i++) {
                List<Integer> subSet = new ArrayList<>(result.get(i));
                subSet.add(num);
                result.add(subSet);
            }
        }

        return result;
    }
}