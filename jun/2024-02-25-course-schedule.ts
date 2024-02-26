function canFinish(numCourses: number, prerequisites: number[][]): boolean {
  const map = {}
  const set = new Set()
  const memo = new Map()

  for(const [course, pre] of prerequisites){
      map[course] = [...(map[course] || []), pre]
  }

  for (const course in map){
      if (!dfs(+course)) {
          return false;
      }
  }

  return true

  function dfs (course: number) {
      if(set.has(course)){
          return false
      }
      if(memo.has(course)){
          return memo.get(course)
      }
      set.add(course)

      if (map[course]) {
          for (const i of map[course]) {
              if (!dfs(i)) {
                  memo.set(course, false)
                  return false;
              }
          }
      }

      set.delete(course)
      memo.set(course, true)
      return true
  }
};