package algs.xuef201806.chap04.direct;
/**
 * 拓扑排序
 * @author moveb
 *
 */
public class Topological {
	private Iterable<Integer> order; // 顶点的拓扑排序
	
	public Topological(Digraph G){
		DirectedCycle cyclefinder = new DirectedCycle(G);
		// 是有向无环图
		if(!cyclefinder.hasCycle()){
			DepthFirstOrder dfs = new DepthFirstOrder(G);
			order = dfs.reversePost();
		}
	}
	/**
	 * 拓扑有序的所有顶点
	 * @return
	 */
	public Iterable<Integer> order(){
		return order;
	}
	/**
	 * G 是有向无环图吗
	 * @return
	 */
	public boolean isDAG(){
		return order != null;
	}
}
