class Solution {

public:

    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {

        unordered_map<int, vector<int>> graph;

        vector<int> degree(numCourses, 0);


        for (auto& req: prerequisites) {

            graph[req[1]].push_back(req[0]);

            degree[req[0]]++;

        }


        queue<int> q;

        for (int i = 0; i < numCourses; i++) {

            if (degree[i]==0) q.push(i);

        }


        while(!q.empty()) {

            int curCour = q.front();

            q.pop();

            numCourses--;


            for (auto& candCour: graph[curCour]) {

                degree[candCour]--;

                if (degree[candCour]==0) q.push(candCour);

            }

        }


        return numCourses==0? true: false;


    }

};

