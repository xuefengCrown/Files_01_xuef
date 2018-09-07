package algs.xuef201806.chap04.weighted;

import algs.base.Bag;
import algs.base.In;

public class EdgeWeightedGraph {
	private int V; // 顶点总数
	private int E; // 边的总数
	private Bag<Edge>[] adj; // 邻接表
	
	// 创建一副含有V个顶点的空图
	public EdgeWeightedGraph(int V){
		this.V = V;
		this.E = 0;
		adj = (Bag<Edge>[])new Bag[V];
		for(int v=0;v<V; v++){
			adj[v] = new Bag<Edge>();
		}
	}
	public EdgeWeightedGraph(In in){
		this(in.readInt()); // 读取 V 并将图初始化
		int E = in.readInt(); // 读取 E
		for(int i=0; i<E; i++){
			// 添加一条边
			int v = in.readInt();
			int w = in.readInt();
			double weight = in.readDouble();
			addEdge(new Edge(v, w, weight));
		}
	}
	public int V() { return V; }
	public int E() { return E; }
	public void addEdge(Edge e){
		int v = e.either(), w = e.other(v);
		adj[v].add(e);
		adj[w].add(e);
		E++;
	}
	public Iterable<Edge> adj(int v){ 
		return adj[v]; 
	}
	public Iterable<Edge> edges(){
		return null;
	}
}
