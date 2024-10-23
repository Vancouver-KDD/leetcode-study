class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int lrow = 0, rrow = matrix.size() - 1, mrow = 0;

        while (lrow <= rrow) {
            mrow = (lrow + rrow) / 2;

            if (target < matrix[mrow][0]) {
                rrow = mrow - 1;
            }
            else if (target > matrix[mrow].back()) {
                lrow = mrow + 1;
            }
            else {
                break;
            }
        }

        if (lrow > rrow) return false;

        int l = 0, r = matrix[mrow].size() - 1;

        while (l <= r) {
            int mid = (l + r) / 2;
            if (matrix[mrow][mid] < target) {
                l = mid + 1;
            }
            else if (matrix[mrow][mid] > target) {
                r = mid - 1;
            }
            else {
                return true;
            }
        }

        return false;
    }
};
