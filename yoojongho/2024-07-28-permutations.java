/**
 * Leetcode
 * problem: 46
 * link: https://leetcode.com/problems/permutations/description/
 * tag: Array, Backtracking
 */

class Solution {
    List<List<Integer>> result;
    int[] src;

    public List<List<Integer>> permute(int[] nums) {
        result = new ArrayList();
        src = nums;
        helper(new ArrayList());
        return result;
    }
    private void helper(List<Integer> temp){
        if(temp.size() == src.length){
            result.add(new ArrayList<>(temp));
        } else {
            for(int i = 0; i < src.length; i++){
                if(temp.contains(src[i])) continue;
                temp.add(src[i]);
                helper(temp);
                temp.remove(temp.size() - 1);
            }
        }
    }
}

/*
example 1:
input: [1,2,3]

depth: 1 | temp: 1          |
depth: 2 | temp: 1, 2       |
depth: 3 | temp: 1, 2, 3    |
depth: 4 | temp: 1, 2, 3    | result: [[1,2,3]]
depth: 3 | temp: 1, 2       |
depth: 2 | temp: 1          |
depth: 2 | temp: 1, 3       |
depth: 3 | temp: 1, 3, 2    |
depth: 4 | temp: 1, 3, 2    | result: [[1,2,3], [1,3,2]]
depth: 3 | temp: 1, 3       |
depth: 2 | temp: 1          |
depth: 1 | temp: 2          |
...
*/