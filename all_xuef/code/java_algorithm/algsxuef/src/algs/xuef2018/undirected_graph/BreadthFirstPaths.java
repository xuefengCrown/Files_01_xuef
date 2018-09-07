package algs.xuef2018.undirected_graph;

import java.util.LinkedList;
import java.util.Queue;

import algs.base.Bag;

public class BreadthFirstPaths {
	private boolean[] marked; // mark visited vertices
	private int[] edgeTo; // keep tree of path
	
	public BreadthFirstPaths(Graph g, int s){
		int V = g.getV();
		marked = new boolean[V];
		for(int v=0; v<V; v++){
			g.getAdj()[v] = new Bag<Integer>();
			marked[v] = false;
		}
		bfs(g, s);
	}
	
	public void bfs(Graph g, int s){
		Queue<Integer> q = new LinkedList<Integer>();
		q.add(s);
		marked[s] = true;
		while(!q.isEmpty()){
			int v = q.poll();
			for(int w:g.adj(v)){
				if(!marked[v]){
					q.add(w);
					marked[w] = true;
					edgeTo[w] = v;
				}
			}
		}
	}
}
