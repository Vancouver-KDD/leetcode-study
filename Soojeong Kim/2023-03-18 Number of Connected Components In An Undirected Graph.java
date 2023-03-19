import java.util.*;

class Graph {
    int V;
    ArrayList<ArrayList<Integer> > adjListArray;
    Graph (int V) {
        this.V =V;
        adjListArray = new ArrayList<>();

        for(int i = 0; i<V;i++) {
            adjListArray.add(i, new ArrayList<>());
        }
    }
    // Adds an edge to an undirected graph
    void addEdge(int src, int dest)
        {
            // Add an edge from src to dest.
            adjListArray.get(src).add(dest);
     
            // Since graph is undirected, add an edge from dest
            // to src also
            adjListArray.get(dest).add(src);
        }
    void DFSUtill(int V, boolean [] visited) {
        //mark current node as visited
        visited[V] = true;
        System.out.println(V + " ");

        for(int x: adjListArray.get(V)){
            if(!visited[x]){
                DFSUtill(x, visited);
            }
        }
    }
    void connectedComponents() {
        boolean[] visited = new boolean[V];
        for(int v = 0; v<V;++v) {
            if(!visited[v]){
                DFSUtill(V, visited);
                System.out.println();
            }
        }
    }
    public static void main(String[] args) {
        Graph g= new Graph(5);

        g.addEdge(1, 0);
        g.addEdge(2, 1);
        g.addEdge(3, 4);

        g.connectedComponents();
    }
}