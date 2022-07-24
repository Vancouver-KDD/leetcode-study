/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {boolean}
 */
var canFinish = function(numCourses, prerequisites) {
    let map = {};
    for (let i=0; i<numCourses; i++){
        map[i] = [];
    }
    
    let visited = {};
    for (let i=0; i<prerequisites.length; i++){
        map[prerequisites[i][0]].push(prerequisites[i][1]);
    }
    
    let dfs = function(prerequisites){
        if(visited[prerequisites]) return false;
        if (map[prerequisites].length==0) return true;
        visited[prerequisites] = true;
        for(let i=0; i<map[prerequisites].length; i++){
            if(!dfs(map[prerequisites][i])) return false;
        }
        delete visited[prerequisites]
        map[prerequisites] = [];
        return true;
    }
    for (let i=0; i<numCourses; i++){
        if(!dfs(i)) return false
    }
    return true;
};
