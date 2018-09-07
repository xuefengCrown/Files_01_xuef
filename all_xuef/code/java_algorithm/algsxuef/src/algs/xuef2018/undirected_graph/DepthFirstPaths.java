package algs.xuef2018.undirected_graph;

import algs.base.Bag;

public class DepthFirstPaths {
	// goal: find all vertices connected to s(and a corresponding path)
	private boolean[] marked; // mark visited vertices
	private int[] edgeTo; // keep tree of path
	
	public DepthFirstPaths(Graph g, int s){
		int V = g.getV();
		marked = new boolean[V];
		for(int v=0; v<V; v++){
			g.getAdj()[v] = new Bag<Integer>();
			marked[v] = false;
		}
		dfs(g, s);
	}
	private void dfs(Graph g, int v){
		marked[v] = true;
		for(int w:g.adj(v)){
			if(!marked[w]){
				dfs(g, w);
				edgeTo[w] = v;
			}
		}
	}
}
