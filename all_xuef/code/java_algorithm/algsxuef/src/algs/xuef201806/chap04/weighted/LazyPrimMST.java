package algs.xuef201806.chap04.weighted;

import algs.base.priorityQueue.MinPQ;
import algs.xuef201806.chap01.Queue;

/**
 * 最小生成树的 Prim 算法的延时实现
 * @author moveb
 *
 */
public class LazyPrimMST {
	private boolean[] marked; // MST vertices
	private Queue<Edge> mst; // MST edges
	private MinPQ<Edge> pq; // 横切边(包括失效边)
	
	public LazyPrimMST(EdgeWeightedGraph G){
		pq = new MinPQ<Edge>();
		marked = new boolean[G.V()];
		mst = new Queue<Edge>();
		visit(G, 0); // assumes G is connected (see Exercise 4.3.22)
		while (!pq.isEmpty())
		{
			Edge e = pq.delMin(); // Get lowest-weight
			int v = e.either(), w = e.other(v); // edge from pq.
			if (marked[v] && marked[w]) // 跳过失效的边
				continue;
			mst.enqueue(e); // Add edge to tree.
			if (!marked[v]) 
				visit(G, v); // Add vertex to tree
			if (!marked[w]) 
				visit(G, w); // (either v or w).
		}
	}
	private void visit(EdgeWeightedGraph G, int v){ 
		// 标记顶点v, 并将所有连接v和未标记顶点的边加入pq
		marked[v] = true;
		for (Edge e : G.adj(v))
		if (!marked[e.other(v)]) 
			pq.insert(e);
	}
	public Iterable<Edge> edges(){ 
		return mst; 
	}
	public double weight(){ 
		// See Exercise 4.3.31.
		return 0.0;
	}
}
