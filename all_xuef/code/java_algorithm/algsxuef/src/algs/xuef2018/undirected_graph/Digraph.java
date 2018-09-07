package algs.xuef2018.undirected_graph;

import algs.base.Bag;
import algs.base.In;

public class Digraph {
	private final int V; // number of vertices
	private Bag<Integer>[] adj; // Adjacency-lists
	
	public Digraph(int V){
		this.V = V;
		adj = (Bag<Integer>[])new Bag[V];
		
		for(int v=0; v<V; v++){
			adj[v] = new Bag<Integer>();
		}
	}
	
	public Digraph(In in)
	{
		this(in.readInt()); // Read V and construct this graph.
		int E = in.readInt(); // Read E.
		for (int i = 0; i < E; i++)
		{ 
			// Add an edge.
			int v = in.readInt(); // Read a vertex,
			int w = in.readInt(); // read another vertex,
			addEdge(v, w); // and add edge connecting them.
		}
	}
	public Bag<Integer>[] getAdj() {
		return adj;
	}

	public void setAdj(Bag<Integer>[] adj) {
		this.adj = adj;
	}

	public int getV() {
		return V;
	}

	// add edge v-w
	public void addEdge(int v, int w){
		adj[v].add(w); // Add w to v’s list.
	}
	
	//iterator for vertices adjacent to v
	public Iterable<Integer> adj(int v){
		return adj[v];
	}
}
