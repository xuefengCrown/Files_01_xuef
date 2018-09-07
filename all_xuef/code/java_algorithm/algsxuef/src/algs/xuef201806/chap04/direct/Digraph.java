package algs.xuef201806.chap04.direct;

import algs.base.In;
import algs.xuef201806.chap01.Bag;

/**
 * 有向图
 * @author moveb
 *
 */
public class Digraph {
	private int V; // 顶点数目
	private int E; // 边的数目
	private Bag<Integer>[] adj; // 邻接表
	
	public Digraph(int V){
		this.V = V;
		this.E = 0;
		adj = (Bag<Integer>[])new Bag[V]; // 创建邻接表
		// 将所有链表初始化
		for(int v=0; v<V; v++){
			adj[v] = new Bag<Integer>();
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
		E++;
	}
	/**
	 * 顶点v指出的边所连接的所有顶点
	 * @param v
	 * @return
	 */
	public Iterable<Integer> adj(int v){
		return adj[v];
	}
	public Digraph reverse(){
		Digraph R = new Digraph(V);
		for(int v=0; v<V; v++){
			for(int w:adj[v]){
				R.addEdge(w, v);
			}
		}
		return R;
	}
}
