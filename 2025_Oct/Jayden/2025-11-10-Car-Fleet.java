class Solution {
    /**
        Time Complexity: O(nlog(n))
        Space Complexity: O(n)
     */
    public int carFleet(int target, int[] position, int[] speed) {
        int n = position.length;

        // 2d array to store cars with its position and speed
        int[][] cars = new int[n][2];

        for (int i = 0; i < position.length; i++) {
            cars[i][0] = position[i];
            cars[i][1] = speed[i];
        }

        // sort 2d array in descending order of the positions
        Arrays.sort(cars, (a, b) -> Integer.compare(b[0], a[0]));

        Stack<Double> fleets = new Stack<>();

        for (int i = 0; i < cars.length; i++) {

            // calculate time for each cars to reach to the target.
            // (target - position) / speed -> m / (m/s) = s (time)
            double timeToTarget = (double)(target - cars[i][0]) / cars[i][1];

            // push only if there's no cars ahead or current car takes less time to reach the target than the car ahead
            if (fleets.isEmpty() || fleets.peek() < timeToTarget) {
                fleets.push(timeToTarget);
            }
        }

        return fleets.size();
    }
}