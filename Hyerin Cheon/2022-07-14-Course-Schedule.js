var canFinish = function (numCourses, prerequisites){
  let visitSet = new Set();
  let preMap = [];

  // create preMap table as empty first
  for(let i = 0; i < numCourses; i++){
    preMap[i] = [];
  }
  // fill numbers on preMap
  for(let [course, dependency] of prerequisites){
    preMap[course].push(dependency);
  }

  function dfs(course){
    if(visitSet.has(course)) return false;

    // empty array means no prerequisites -> can be completed
    if(preMap[course].length == 0) return true;
    visitSet.add(course);

    for(let dependency of preMap[course]){
      if(!dfs(dependency)) return false;
    }
    
    // don't understand this part, if we delete the course how can we detect if this graph is cycle or not
    // or do i need to delete only for dependency..?
    visitSet.delete(course)

    // change to empty array, since we know this course can be completed
    preMap[course] = [];
    return true;
  }
  for(let i = 0; i < numCourses; i++){
    if(!dfs(i)) return false;
  }
  return true;
}