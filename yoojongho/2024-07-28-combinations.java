/**
 * Leetcode
 * problem: 77
 * link: https://leetcode.com/problems/combinations/description/
 * tag: Backtracking
 */

/**
 * use backtracking
 *
 */

class Solution {
    List<List<Integer>> result;
    int range;
    int size;
    public List<List<Integer>> combine(int n, int k) {
        result = new ArrayList<>();
        range = n;
        size = k;
        helper(new ArrayList(), 0);
        return result;
    }

    private void helper(List<Integer> temp, int flag){
        flag++;
        if(temp.size() == size){
            result.add(new ArrayList(temp));
            return;
        }
        for(int i = flag; i <= range; i++){
            temp.add(i);
            helper(temp, i);
            temp.remove(temp.size() - 1);
        }
    }
}