// Author: Juyoung Moon

// KDD LeetCode Study Week 12: Graph (BFS/DFS/Union)
// https://github.com/juyomo/leetcode-study

// LeetCode #417.
// https://leetcode.com/problems/pacific-atlantic-water-flow/

class Solution {
public:
    const int kUnvisited = 0;
    const int kReachable = 1;
    const int kUnreachable = -1;

    void search(const vector<vector<int>>& originalMap, vector<vector<int>>& res, queue<pair<int, int>>& tovisit) {
        int height = originalMap.size();
        int width = originalMap[0].size();
        
        int dr[] = {-1, 0, 1, 0};
        int dc[] = {0, -1, 0, 1};

        while (!tovisit.empty()) {
            auto curr = tovisit.front();
            tovisit.pop();
            int oldr = curr.first;
            int oldc = curr.second;
            res[oldr][oldc] = kReachable;

            for (int i = 0; i < 4; i++) {
                int nr = oldr + dr[i];
                int nc = oldc + dc[i];
                if (nr >= 0 && nc >= 0 && nr < height && nc < width && res[nr][nc] != kReachable) {
                    if (originalMap[nr][nc] >= originalMap[oldr][oldc]) {
                        res[nr][nc] = kReachable;
                        tovisit.push(make_pair(nr, nc));
                    }
                }
            }
        }
    }
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        int height = heights.size();
        int width = heights[0].size();

        vector<vector<int>> fromAtlantic(height, vector<int>(width, kUnvisited));
        vector<vector<int>> fromPacific(height, vector<int>(width, kUnvisited));
        queue<pair<int, int>> tovisitA;
        queue<pair<int, int>> tovisitP;
        
        for (int r = 0; r < height; r++) {
            tovisitA.push(make_pair(r, width - 1));    
        }
        for (int c = 0; c < width - 1; c++) {
            tovisitA.push(make_pair(height - 1, c));
        }

        for (int r = 0; r < height; r++) {
            tovisitP.push(make_pair(r, 0));    
        }
        for (int c = 1; c < width; c++) {
            tovisitP.push(make_pair(0, c));
        }

        search(heights, fromAtlantic, tovisitA);
        search(heights, fromPacific, tovisitP);

        vector<vector<int>> res;

        for (int i = 0; i < height; i++) {
            for (int j = 0; j < width; j++) {
                if (fromAtlantic[i][j] == kReachable && fromPacific[i][j] == kReachable) {
                    res.push_back({i, j});
                }
            }
        }

        return res;
    }
};
