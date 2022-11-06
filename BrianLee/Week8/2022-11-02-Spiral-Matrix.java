class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> result = new LinkedList<>();
        move(matrix, 0, 0, 0, result);
        return result;
    }

    private void move(int[][] matrix, int x, int y, int direction, List<Integer> result) {
        if(0 > x || x >= matrix.length) return;
        if(0 > y || y >= matrix[0].length) return;
        if(matrix[x][y] == 101) return;

        result.add(matrix[x][y]);
        matrix[x][y] = 101;

        // direction = 0 = right
        if(direction == 0) {
            move(matrix, x, y+1, direction, result);
            move(matrix, x+1, y, direction+1, result);
        } else if(direction == 1) {
            // direction = 1 = down
            move(matrix, x+1, y, direction, result);
            move(matrix, x, y-1, direction+1, result);
        } else if(direction == 2) {
            // direction = 2 = left
            move(matrix, x, y-1, direction, result);
            move(matrix, x-1, y, direction+1, result);
        } else {
            // direction = 3 = up
            move(matrix, x-1, y, direction, result);
            move(matrix, x, y+1, 0, result);
        }
    }
}