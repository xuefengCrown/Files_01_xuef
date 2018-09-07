package algs.xuef201806.chap04;

import algs.base.In;
import algs.xuef201806.chap01.Bag;

/**
 * 邻接矩阵表示的无向图
 * @author moveb
 *
 */
public class UndirectGraph {
	private int V; // 顶点数目
	private int E; // 边的数目
	private Bag<Integer>[] adj; // 邻接表
	
	public UndirectGraph(int V){
		this.V = V;
		this.E = 0;
		adj = (Bag<Integer>[])new Bag[V]; // 创建邻接表
		// 将所有链表初始化
		for(int v=0; v<V; v++){
			adj[v] = new Bag<Integer>();
		}
	}
	public UndirectGraph(In in){
		this(in.readInt()); // 读取 V 并将图初始化
		int E = in.readInt(); // 读取 E
		for(int i=0; i<E; i++){
			// 添加一条边
			int v = in.readInt();
			int w = in.readInt();
			addEdge(v, w);
		}
	}
	public UndirectGraph(In in, int V, int E){
		this(V); // 读取 V 并将图初始化
		for(int i=0; i<E; i++){
			// 添加一条边
			int v = in.readInt();
			int w = in.readInt();
			addEdge(v, w);
		}
	}
	public int V(){
		return V;
	}
	public int E(){
		return E;
	}
	public void addEdge(int v, int w){
		adj[v].add(w);
		adj[w].add(v);
		E++;
	}
	/**
	 * 返回节点v的所有相邻节点
	 * @param v
	 * @return
	 */
	public Iterable<Integer> adj(int v){
		return adj[v];
	}
}
