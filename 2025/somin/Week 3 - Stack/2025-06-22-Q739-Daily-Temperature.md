```

public class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int n = temperatures.length;
        int[] answer = new int[n];
        Stack<Integer> stack = new Stack<>(); // 인덱스를 저장

        for (int i = 0; i < n; i++) {
            // 현재 온도가 스택 top보다 높으면 → 결과 계산
            while (!stack.isEmpty() && temperatures[i] > temperatures[stack.peek()]) {
                int prevIndex = stack.pop();
                answer[prevIndex] = i - prevIndex; // 몇 일 뒤인지 계산
            }
            stack.push(i); // 현재 인덱스를 스택에 추가
        }

        return answer;
    }
}

```
