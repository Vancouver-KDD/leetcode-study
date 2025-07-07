

```

import java.util.*;

public class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        Stack<Integer> stack = new Stack<>();

        for (int a : asteroids) {
            boolean alive = true;

            // 충돌 조건: 스택 top이 오른쪽(+), 현재 asteroid는 왼쪽(-)
            while (alive && !stack.isEmpty() && stack.peek() > 0 && a < 0) {
                int top = stack.peek();
                if (top < -a) {
                    // 스택 top이 작아서 폭발, 계속 다음 충돌 확인
                    stack.pop();
                } else if (top == -a) {
                    // 둘 다 폭발
                    stack.pop();
                    alive = false;
                } else {
                    // 현재 소행성(a)이 작아서 폭발
                    alive = false;
                }
            }

            if (alive) {
                stack.push(a);
            }
        }

        // 결과 반환
        int[] result = new int[stack.size()];
        for (int i = result.length - 1; i >= 0; i--) {
            result[i] = stack.pop();
        }
        return result;
    }
}

```
