package algs.xuef201806.chap04.direct;
/**
 * 有向图的可达性
 * @author moveb
 * 深度优先搜索本质上是一种适用于处理有向图的算法?!
 */
public class DigraphDFS {
	private boolean[] marked;
	
	/**
	 * 在G中找到从s可达的所有顶点
	 * @param G
	 * @param s
	 */
	public DigraphDFS(Digraph G, int s){
		marked = new boolean[G.V()];
		dfs(G, s);
	}
	private void dfs(Digraph G, int v){
		marked[v] = true;
		for(int w:G.adj(v)){
			if(!marked[w])
				dfs(G, w);
		}
	}
	
	/**
	 * 在G中找到从sources中的所有顶点可达的所有顶点
	 * @param G
	 * @param sources
	 */
	public DigraphDFS(Digraph G, Iterable<Integer> sources){
		marked = new boolean[G.V()];
		for(int s:sources){
			if(!marked[s])
				dfs(G, s);
		}
	}
}
