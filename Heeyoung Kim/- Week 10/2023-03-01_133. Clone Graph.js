let cloneGraph = (graph) => {
    let start = node; 
    if (start === null) return null;
    const vertexMap = new Map(); 
    const queue = [start]
    vertexMap.set(start, new Node(start.val)); 
    while (queue.length > 0) {
        const currentVertex = queue.shift(); 
        for (const neighbor of currentVertex.neighbors) { s
            if (!vertexMap.has(neighbor)) {
                vertexMap.set(neighbor, new Node(neighbor.val))
                queue.push(neighbor); 
            }
            vertexMap.get(currentVertex).neighbors.push(vertexMap.get(neighbor)); 
        }
    }
   return vertexMap.get(start); 
}