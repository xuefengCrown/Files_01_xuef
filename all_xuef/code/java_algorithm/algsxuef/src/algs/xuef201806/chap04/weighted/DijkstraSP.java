package algs.xuef201806.chap04.weighted;

import algs.base.priorityQueue.IndexMinPQ;
import algs.xuef201806.chap01.Stack;

public class DijkstraSP {
	private DirectedEdge[] edgeTo;
	private double[] distTo; // source到所有节点的最短距离
	/**
	 * 保存需要被放松的顶点并确认下一个被放松的顶点
	 */
	private IndexMinPQ<Double> pq;
	
	public DijkstraSP(EdgeWeightedDigraph G, int s){
		edgeTo = new DirectedEdge[G.V()];
		distTo = new double[G.V()];
		pq = new IndexMinPQ<Double>(G.V());
		/**
		 * 将 distTo[]的其他元素初始化正无穷
		 * distTo[s]初始化为0
		 */
		for (int v = 0; v < G.V(); v++)
			distTo[v] = Double.POSITIVE_INFINITY;
		
		distTo[s] = 0.0;
		
		pq.insert(s, 0.0);
		while (!pq.isEmpty())
			// Removes a minimum key and returns its associated index.
			// 删除key最小的, 返回关联的索引
			relax(G, pq.delMin());
	}
	private void relax(EdgeWeightedDigraph G, int v){
		for(DirectedEdge e : G.adj(v)){
			int w = e.to();
			if (distTo[w] > distTo[v] + e.weight()){
				// 说明, s-->v-->w 比之前存储的s-->w更短; 要更新 distTo[w]
				distTo[w] = distTo[v] + e.weight();
				// 将 v-->w 加入最短路径树
				edgeTo[w] = e;
				// 将节点v指向的所有节点放入pq中
				if (pq.contains(w)) 
					pq.change(w, distTo[w]);
				else 
					pq.insert(w, distTo[w]);
			}
		}
	}
	public double distTo(int v){
		// standard client query methods
		return distTo[v];
	}
	public boolean hasPathTo(int v){
		// for SPT implementatations
		return distTo[v] < Double.POSITIVE_INFINITY;
	}
	public Iterable<DirectedEdge> pathTo(int v){
		if(!hasPathTo(v)) return null;
		Stack<DirectedEdge> path = new Stack();
		for(DirectedEdge e = edgeTo[v]; e != null; e = edgeTo[e.from()]){
			path.push(e);
		}
		return path;
	}
}
