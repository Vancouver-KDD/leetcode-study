class Solution {
public:
    int guessNumber(int n) {
        int left = 1;
        int right = n;

        while (left <= right) {
            // int overflow 방지
            int mid = left + (right - left) / 2;
            int res = guess(mid);

            if (res == 0) {
                return mid;  // 정답을 찾음
            }
            else if (res < 0) {
                right = mid - 1;  // pick < mid
            }
            else {
                left = mid + 1;   // pick > mid
            }
        }

        return -1;  // 이론상 도달하지 않음 (pick은 항상 1~n 사이)
    }
};