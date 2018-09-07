package algs.xuef201806.chap04;

import algs.base.Point2D;
import algs.base.StdDraw;
import algs.base.StdRandom;
import algs.xuef201806.chap01.Queue;

/**
 * 广度优先搜索
 * @author moveb
 *
 */
public class BreadthFirstPaths {
	private boolean[] marked;
	private int[] edgeTo;
	private int s; // source
	
	public Point2D[] points;
	
	public BreadthFirstPaths(UndirectGraph G, int s, Point2D[] p){
		marked = new boolean[G.V()];
		edgeTo = new int[G.V()];
		this.s = s;
		
		points = p;
		
		bfs(G, s);
	}
	public void bfs(UndirectGraph G, int s){
		marked[s] = true;
		Queue<Integer> queue = new Queue();
		queue.enqueue(s);
		
		StdDraw.setPenRadius(0.002);//.0002
		StdDraw.setPenColor(StdDraw.BLACK);
		
		while(!queue.isEmpty()){
			
			// 从队列中取出节点
			int v = queue.dequeue();
			for(int w : G.adj(v)){
				if(!marked[w]){
					edgeTo[w] = v;
					marked[w] = true;
					queue.enqueue(w);
					
					points[v].drawTo(points[w]);
					try {
						Thread.sleep(100);
					} catch (InterruptedException e) {
						e.printStackTrace();
					}
				}
			}
		}
	}
}
