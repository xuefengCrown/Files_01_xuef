package algs.xuef201806.chap04;
/**
 * 使用深度优先搜索找出图中的所有连通分量
 * @author moveb
 *
 */
public class CC {
	private boolean[] marked;
	// 以顶点作为索引的数组, 将同一个连通分量中的顶点与连通分量的标识符(int值)关联起来
	// 它使得connected()方法的实现变得十分简单(只需检查标识符是否相同)
	private int[] id; 
	private int count; // 连通分量标识符
	
	public CC(UndirectGraph G){
		marked = new boolean[G.V()];
		id = new int[G.V()];
		/**
		 * 第一次调用 dfs(G, 0)
		 * 会标记所有与0连通的顶点
		 */
		for(int s=0; s<G.V(); s++){ // 遍历所有顶点
			if(!marked[s]){
				dfs(G, s);
				count++;
			}
		}
	}
	private void dfs(UndirectGraph G, int v){
		marked[v] = true;
		id[v] = count;
		for(int w:G.adj(v)){
			if(!marked[w]){
				dfs(G, w);
			}
		}
	}
	public boolean connected(int v, int w){
		return id[v] == id[w];
	}
	public int id(int v){
		return id[v];
	}
	public int count(){
		return count;
	}
}
