//2022.10.22

//input: 1 ,[]  -> Output: true

//아래 Time Complexity 랑 Space complexity 내용이 헷갈리는데???
//Time Complexity: O(E + V) <- V: the number of courses, E: the number of dependencies
//Space Complexity: O(E + V) 
class Solution {

    private HashMap<Integer, List<Integer>> coursesMap = new HashMap<Integer, List<Integer>>();
    private boolean[] checked;
    private boolean[] visited;
        
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        if(numCourses < 1 || prerequisites == null){
            return false; //??
        }
        
        if(prerequisites.length <= 1){ // no prerequisite or only one prerequisite
            return true;
        }
        
        checked = new boolean[numCourses];
        visited = new boolean[numCourses];
        
        //make prerequisite course map.
        for(int[] prerequisite : prerequisites){
            int course = prerequisite[0];
            int preCourse = prerequisite[1];
            
            if(coursesMap.containsKey(course)){
                //System.out.println("List:" + coursesMap.get(course));
                coursesMap.get(course).add(preCourse);
            }else{
                List<Integer> courseList = new ArrayList<Integer>(Arrays.asList(preCourse));
                coursesMap.put(course, courseList);
            }            
        }
        
        //Check whether there is a cycle. 
        for(int i = 0; i < numCourses; i++){
            if(isCycle(i)){
                return false;
            }
        }
        
        return true;
    }
    
    private boolean isCycle(int numCourse){
        //System.out.println("[isCycle]numCourse:" + numCourse);
        if(checked[numCourse]){
            //System.out.println("_1_");
            return false; //already checked - no cycle
        }
        
        if(visited[numCourse]){
            //System.out.println("_2_");
            return true;  //already visited - it means, cycle happens
        }
        
        if(!coursesMap.containsKey(numCourse)){
            //System.out.println("_3_");
            return false; // there is no prerequisite - no cycle. 
        }
        
        List<Integer> prerequisites = coursesMap.get(numCourse);
        
        visited[numCourse] = true;
        for(int prereq : prerequisites){
            if(isCycle(prereq)){
                //System.out.println("_4_prereq:" + prereq);
                return true; // there is cycle.
            }
        }
        visited[numCourse] = false;
        
        checked[numCourse] = true;
        return false;
    }
}
