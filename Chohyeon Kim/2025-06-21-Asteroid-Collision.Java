class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        // + ->
        // - <-
        // [-1,5,10,-5]
        // 
        // + -> stacking 
        // - -> pop from the stack if empty put into stack
        // -> pop from stack but - then put into stack
        // [-1, 10]

        // -
        // 1) if stack is empty, push into stack
        // 2) top of stack is Negative, push a into stack. break out of loop
        // 3) top of stack is Positive but less than a, destrory top and move to the next one (keep going)
        // 4) top of stack is positive but top = a they dont destroyed and break out of loop
        // 5) top of stack is positive but more than a, a is distroyed and put top back into stack and break out of loop

        Deque<Integer> stack = new ArrayDeque<>();

        for (int a : asteroids) {

            if (a > 0) {
                stack.push(a);
            } else {

                // stack is empty -> push -a                
                if (stack.isEmpty()) {
                    stack.push(a);
                    continue;
                }


                while (true) {

                    if (stack.isEmpty()) {
                        stack.push(a);
                        break;
                    } else if (stack.peek() < 0) {
                        stack.push(a);
                        break;
                    } else if (stack.peek() < -a) {
                        stack.pop();
                    } else if (stack.peek() == -a) {
                        stack.pop();
                        break;
                    } else {
                        break;
                    }

                }

            }

            // System.out.print(stack.toString());    

        }

        int[] res = new int[stack.size()];

        for (int i = stack.size() - 1; i >= 0; i--) {

            res[i] = stack.pop();

        }

        return res;
        
    }
}