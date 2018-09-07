package algs.xuef2018.undirected_graph;

import algs.base.Bag;
import algs.base.In;
/*
 * tinyG.txt
    13 //V
	13 //E
	0 5
	4 3
	0 1
	9 12
	6 4
	5 4
	0 2
	11 12
	9 10
	0 6
	7 8
	9 11
	5 3
 */
/**
 * Adjacency-lists 
 * represent undirected graph
 * @author moveb
 *
 */
public class Graph {
	private final int V; // number of vertices
	private int E; // number of edges
	private Bag<Integer>[] adj; // Adjacency-lists
	
	public Graph(int V){
		this.V = V; this.E = 0;
		adj = (Bag<Integer>[])new Bag[V];
		
		for(int v=0; v<V; v++){
			adj[v] = new Bag<Integer>();
		}
	}
	
	public Graph(In in)
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
		adj[w].add(v);
		E++;
	}
	
	//iterator for vertices adjacent to v
	public Iterable<Integer> adj(int v){
		return adj[v];
	}
}
