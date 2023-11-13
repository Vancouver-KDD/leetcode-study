class Solution {
    // Directions for going clockwise: 0: 'up', 1: 'right', 2: 'down', 3: 'left'
    int[][] directions = { { -1, 0 }, { 0, 1 }, { 1, 0 }, { 0, -1 } };
    Set<Pair<Integer, Integer>> visited = new HashSet<>();
    Robot robot;

    // Move the robot backward
    public void goBack() {
        robot.turnRight();
        robot.turnRight();
        robot.move();
        robot.turnRight();
        robot.turnRight();
    }

    // Backtrack and explore the room
    public void backtrack(int row, int col, int d) {
        visited.add(new Pair<>(row, col));
        robot.clean();

        // Explore in all four directions
        for (int i = 0; i < 4; ++i) {
            int newD = (d + i) % 4;
            int newRow = row + directions[newD][0];
            int newCol = col + directions[newD][1];

            // Check if the new cell is not visited and the robot can move to that cell
            if (!visited.contains(new Pair<>(newRow, newCol)) && robot.move()) {
                backtrack(newRow, newCol, newD);
                goBack();
            }

            // Turn the robot following the chosen direction: clockwise
            robot.turnRight();
        }
    }

    // Clean the entire room using backtracking
    public void cleanRoom(Robot robot) {
        this.robot = robot;
        backtrack(0, 0, 0);
    }
}