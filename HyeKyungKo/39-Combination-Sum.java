// 아래 솔루션을 iteration 으로는 푸는 방법을 모르겠다. 풀수 있는지조차 모르겠다. 
// leetcode 솔루션에도 recursive 만 나와있음. 

//2022-12-04 - recursive : DP-Top down
//Time Complexity:  O(N^(target/min + 1)) <- N is candidates.length, 
//        min is the minimum number of candidates.  target/min + 1 = tree height
//        매 트리마다 sub tree 에서 다시 candidates 를  체크함. ( 정확히는 1개씩 줄어든 candidates 이긴 하다.) 
​//Space Complexity: O(target/min)  <-- recursive calls stack 은 tree의 height
class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<>();
        if(candidates == null || candidates.length == 0 || target <= 0){
            return result;
        }   

        LinkedList<Integer> comb = new LinkedList<>();
        findCombination(candidates, target, comb, 0, result);     

        return result;
    }

    private void findCombination(int[] candidates, int target, LinkedList<Integer> comb, int start, List<List<Integer>> result){

        if(target < 0){
            return;
        }
        if(target == 0){ //find combination
            result.add(new ArrayList<>(comb));
        }

        for(int i = start; i < candidates.length; i++){
            comb.add(candidates[i]);
            findCombination(candidates, target - candidates[i], comb, i, result);
            comb.removeLast();
        }
    }
}
