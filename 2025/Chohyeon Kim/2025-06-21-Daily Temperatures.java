import java.util.*;

record Pair (int value, int index) {}

class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        // monotonically decreasing stack
        // find the next greater or smaller element in the array

        // [73,74,75,71,69,72,76,73]
        // output = [1 1 4 2 1 1 0 0]
        // stack = [(76, 6) (73, 7)]
        // 

        int n = temperatures.length;
        int[] res = new int[n];

        Deque<Pair> stack = new ArrayDeque<>();


        for (int i = 0; i < temperatures.length; i++) {

            int temp = temperatures[i];

            if (stack.isEmpty()) {
                stack.push(new Pair(temp, i));
                continue;
            }

            while (true) {

                Pair top = stack.peek();

                if (stack.isEmpty()){
                    stack.push(new Pair(temp, i));
                    break;
                } else {

                    if (top.value() < temp) {
                        Pair prev = stack.pop();
                        res[prev.index()] = i - prev.index();
                        continue;
                    } else {
                        stack.push(new Pair(temp, i));
                        break;
                    }

                }

            }
        }


        return res;


