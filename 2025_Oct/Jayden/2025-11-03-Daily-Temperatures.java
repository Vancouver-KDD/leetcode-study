class Solution {
    /**
        Time Complexity: O(n)
        Space Complexity: O(n)
     */
    public int[] dailyTemperatures(int[] temperatures) {
        Stack<Integer> stack = new Stack<>();
        int[] result = new int[temperatures.length];

        for (int i = 0; i < temperatures.length; i++) {

            // for new temperture encountered, pop elements in stack untill that has less temperture than itself.
            while (!stack.isEmpty() && temperatures[i] > temperatures[stack.peek()]) {

                // i - stack.pop() calculates the distance between the temperatures
                result[stack.peek()] = i - stack.pop();

            }
            stack.push(i);
        }

        return result;
    }
}