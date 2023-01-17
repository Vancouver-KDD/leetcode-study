// BFS and Kahn's Algorithm
class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        
        // seek cycle in graph
        // let each element in prereq be a node of graph
        // prerequisites[0] is dependent on prerequistes[1]
        //      => edge from prerequisites[1] to prerequisites[0]
        // if any two elements direct each other, cycle formed (will not be able to take course)
        
        vector<int> deg(numCourses,0);
        vector<int> adj[numCourses];
        
        for(auto p:prerequisites){
            adj[p[1]].push_back(p[0]);
            deg[p[0]]++;
        }
        
        queue<int> q;
        
        // Kahn's algorithm
        // sort elements in graph in topological order
        // if there exists a cycle, elements not sorted and process broken
        
        for(int i=0; i<numCourses; ++i){
            if(deg[i]==0) q.push(i);
        }
        
        // count for processed elements
        int count = 0;
        while(!q.empty()){
            int node = q.front();
            q.pop();
            count++;
            
            for(auto it:adj[node]){
                if(deg[it]!=0) deg[it]--;
                if(deg[it]==0) q.push(it);
            }
        }
        // if count != numCourses return false
        return count==numCourses ? true : false;
    }
};
