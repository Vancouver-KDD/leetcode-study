// Author: Juyoung Moon
// Solved on Mon, June 23, 2025 (KST).

// KDD LeetCode Study Week 3: Stack.
// https://github.com/juyomo/leetcode-study

// LeetCode #735.
// https://leetcode.com/problems/asteroid-collision/

class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        vector<int> res;
        for (int i = 0; i < asteroids.size(); i++) {
            int curr = asteroids[i];
            if (res.empty() || curr > 0) {
                res.push_back(curr);
                continue;
            }

            bool done = false;
            while (!res.empty() && !done) {
                if (res.back() < 0) {
                    res.push_back(curr);
                    done = true;
                } else if (res.back() + curr == 0) {
                    res.pop_back();
                    done = true;
                } else if (res.back() + curr > 0) {
                    done = true;
                } else if (res.back() + curr < 0) {
                    res.pop_back();
                }
            }
            if (!done) {
                res.push_back(curr);
            }
        }
        return res;
    }
};
