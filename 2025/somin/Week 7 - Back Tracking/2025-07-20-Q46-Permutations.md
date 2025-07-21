```
import java.util.*;

class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();  // 결과를 담을 리스트
        List<Integer> path = new ArrayList<>();          // 현재까지 선택한 숫자들
        boolean[] used = new boolean[nums.length];       // 숫자가 사용되었는지 체크

        dfs(nums, path, used, result);                   // 탐색 시작
        return result;
    }

    // 재귀 함수
    void dfs(int[] nums, List<Integer> path, boolean[] used, List<List<Integer>> result) {
        // 종료 조건: 모든 숫자를 선택한 경우
        if (path.size() == nums.length) {
            result.add(new ArrayList<>(path));           // 현재 순열을 결과에 추가
            return;
        }

        // 가능한 모든 숫자를 탐색
        for (int i = 0; i < nums.length; i++) {
            if (used[i]) continue;                       // 이미 사용한 숫자는 건너뛰기

            // i번째 숫자 선택
            path.add(nums[i]);
            used[i] = true;                              // 사용 표시

            dfs(nums, path, used, result);               // 다음 단계로 재귀 호출

            // 백트래킹: 선택 취소
            path.remove(path.size() - 1);
            used[i] = false;
        }
    }
}
```
