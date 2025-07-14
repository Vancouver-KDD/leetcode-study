class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        Stack<Integer> stack = new Stack<>();

        for (int asteroid : asteroids) {
            boolean alive = true;

            while (!stack.isEmpty() && asteroid < 0 && stack.peek() > 0) {
                int top = stack.peek();
                if (top < -asteroid) {
                    stack.pop();      
                } else if (top == -asteroid) {
                    stack.pop();      
                    alive = false;
                    break;
                } else {
                    alive = false;   
                    break;  
                }
            }

            if (alive) {
                stack.push(asteroid); 
            }
        }

        // 스택을 배열로 변환
        int[] result = new int[stack.size()];
        for (int i = stack.size() - 1; i >= 0; i--) {
            result[i] = stack.pop();
        }

        return result;
    }
}
