import java.util.*;

class asteroidCollision {
    public int[] asteroidCollision(int[] asteroids) {
        
        Stack<Integer> stack = new Stack<>();

        for (Integer a : asteroids){
            boolean alive = true;
            
            while (alive && !stack.isEmpty() && stack.peek()>0 && a<0){
                int b = stack.peek();

                if (-a>b){
                    stack.pop();
                } else if (-a==b){
                    stack.pop();
                    alive = false;
                } else{
                    alive = false;
                }
            }

            if (alive) {
                stack.push(a);
            }
        }

        int[] result = new int[stack.size()];
        for (int i = 0; i < stack.size(); i++) {
            result[i] = stack.get(i);
        }

        return result;
    }
}