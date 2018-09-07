package algs.xuef201806.chap04.weighted;
/**
 * 加权有向边
 * @author moveb
 *
 */
public class DirectedEdge {
	private final int v; // one vertex
	private final int w; // the other vertex
	private final double weight; // edge weight
	public DirectedEdge(int v, int w, double weight){
		this.v = v;
		this.w = w;
		this.weight = weight;
	}
	
	public double weight(){ 
		return weight; 
		}
	public int from(){ 
		return v; 
	}
	public int to(){ 
		return w; 
	}
	public String toString(){ 
		return String.format("%d-%d %.2f", v, w, weight); 
	}
}
