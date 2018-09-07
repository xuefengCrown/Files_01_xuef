package algs.xuef201806.chap04;
/**
 * 深度优先搜索
 * @author moveb
 *
 */
public class DepthFirstSearch {
	private boolean[] marked;
	private int count;
	
	public DepthFirstSearch(UndirectGraph G, int s){
		marked = new boolean[G.V()];
		dfs(G, s);
	}
	
	private void dfs(UndirectGraph G, int v){
		marked[v] = true;
		count++;
		for(int w : G.adj(v)){
			if(!marked[w])
				dfs(G, w);
		}
	}
	
	public boolean marked(int w){
		return marked[w];
	}
	public int count(){
		return count;
	}
}
