// Use Kahn's algorithm to see if a topological ordering is possible
// In this problem each item in the prequisites array comes in the form [a,b], were b is the course you need to take first before you can take a
var canFinish = function(numCourses, prerequisites) {
    // Initialize an array that holds the counts of how many times each course was an 'a'
    // which means you needed to take another course before you could take it
    // If imagined as a graph, these courses all have edges going into them from some other vertex and the count represents the total number of edges going into each one
    const inDegree = new Array(numCourses).fill(0);
    // Count how many times each course is an 'a'
    // Each course count will be placed at a corresponding index in the inDegree array
    for(const pre of prerequisites) {
        inDegree[pre[0]]++
    }
    // Initialize array of courses that have no prerequisites, these will always be in the 'b' position of the [a,b] group
    // If imagined as a graph, these courses will have no edges pointing into them
    const zeroDegree = [];
    // If no prerequisites were found for a course it's count will be 0
    // Add these to the zeroDegree array
    for(let i = 0; i < numCourses; i++) {
        if(inDegree[i]===0) {
            zeroDegree.push(i);
        }
    }
    // If the zeroDegree array is empty, that means there is no heirarchical relation because you cannot not take a single course without needing to take another one first
    if(zeroDegree.length === 0) return false;

    // Loop through the zeroDegree array
    while(zeroDegree.length) {
        // Remove a course from the array on every iteration
        const course = zeroDegree.pop();
        // Account for all the times in the prerequisites array that this course was a precourse to another course, i.e. course was in the 'b' position
        for(const pre of prerequisites) {
            if(course === pre[1]) {
                // Subtract from the count of the 'a' course matched
                inDegree[pre[0]]--
                // If the 'a' course in this relationship is 0 in the inDegree array, that means we have accounted for all the times it was used
                // If imagined as a graph, we have accounted for all edges leading into this vertex
                if(inDegree[pre[0]]===0) {
                    // Push this course into the zeroDegree and see if it is needed as a precourse for any other courses
                    // If imagined as a graph, see if this vertex has an edge that points into another vertix
                    zeroDegree.push(pre[0])
                }
            }
        }
    }
    // If there is any index in the array that is not 0, that means there is a precourse relationship that is unaccounted for
    for(const num of inDegree) {
        if(num!== 0) return false
    }
    return true;
};
