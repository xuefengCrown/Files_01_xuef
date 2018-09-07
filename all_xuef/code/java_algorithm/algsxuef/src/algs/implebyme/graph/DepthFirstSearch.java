package algs.implebyme.graph;

public class DepthFirstSearch{
	private boolean[] marked;
	private int count;
	public DepthFirstSearch(Graph G, int s){
		marked = new boolean[G.V()]; // 将节点设置为 未标记（访问）
		dfs(G, s);
	}
	private void dfs(Graph G, int v){
		marked[v] = true;
		count++;
		for (int w : G.adj(v))
			if (!marked[w]) dfs(G, w);
	}
	public boolean marked(int w){ 
		return marked[w]; 
	}
	public int count(){ 
		return count; 
	}
}
