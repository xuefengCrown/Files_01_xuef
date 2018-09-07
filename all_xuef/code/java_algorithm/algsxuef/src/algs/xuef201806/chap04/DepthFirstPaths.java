package algs.xuef201806.chap04;

import java.util.Stack;

/**
 * Depth-first search to find paths in a graph
 * @author moveb
 *
 */
public class DepthFirstPaths {
	private boolean[] marked;
	private int[] edgeTo; // last vertex on known path to this vertex
	private final int s; // source
	public DepthFirstPaths(UndirectGraph G, int s){
		marked = new boolean[G.V()];
		edgeTo = new int[G.V()];
		this.s = s;
		
		dfs(G, s);
	}
	
	private void dfs(UndirectGraph G, int v){
		marked[v] = true;
		for(int w : G.adj(v)){
			if(!marked[w]){
				edgeTo[w] = v;
				dfs(G, w);
			}
		}
	}
	/**
	 * source 到 v是否相通
	 * @param v
	 * @return
	 */
	public boolean hasPathTo(int v){
		return marked[v];
	}
	/**
	 * 到 v 的路径
	 * @param v
	 * @return
	 */
	public Iterable<Integer> pathTo(int v){
		if(!hasPathTo(v)) return null;
		Stack<Integer> path = new Stack<Integer>();
		for(int x=v; x!=s; x=edgeTo[x]){
			path.push(x);
		}
		path.push(s);
		return path;
	}
	
	/**
	 * v 到 source的步数
	 * @param v
	 * @return
	 */
	public int stepsTo(int v){
		if(!hasPathTo(v)) return 0;
		Stack<Integer> path = new Stack<Integer>();
		for(int x=v; x!=s; x=edgeTo[x]){
			path.push(x);
		}
		path.push(s);
		
		return path.size();
	}
}
