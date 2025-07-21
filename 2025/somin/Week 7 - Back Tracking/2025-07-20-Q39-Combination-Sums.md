```
import java.util.*;

class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<>();   // 결과를 담을 리스트
        List<Integer> path = new ArrayList<>();           // 현재까지 선택한 숫자들

        dfs(candidates, target, 0, path, result);         // 탐색 시작
        return result;
    }

    // 재귀 함수
    void dfs(int[] candidates, int target, int start, List<Integer> path, List<List<Integer>> result) {
        // 종료 조건: 합이 0이 된 경우 → 유효한 조합
        if (target == 0) {
            result.add(new ArrayList<>(path));            // 현재 조합을 결과에 추가
            return;
        }

        // 종료 조건: 합이 0보다 작아지면 → 잘못된 경로
        if (target < 0) {
            return;
        }

        // 후보 숫자들을 탐색
        for (int i = start; i < candidates.length; i++) {
            path.add(candidates[i]);                      // 현재 숫자 선택
            // 같은 숫자를 다시 선택할 수 있으므로 start 대신 i를 넘긴다
            dfs(candidates, target - candidates[i], i, path, result);

            path.remove(path.size() - 1);                 // 선택 취소 (backtracking)
        }
    }
}

```
