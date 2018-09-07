package algs.xuef201806.chap04.weighted;
/**
 * 带权重的边
 * @author moveb
 *
 */
public class Edge implements Comparable<Edge> {
	private final int v; // one vertex
	private final int w; // the other vertex
	private final double weight; // edge weight
	public Edge(int v, int w, double weight){
		this.v = v;
		this.w = w;
		this.weight = weight;
	}
	public double weight(){ 
		return weight; 
		}
	public int either(){ 
		return v; 
	}
	public int other(int vertex){
		if (vertex == v) return w;
		else if (vertex == w) return v;
		else throw new RuntimeException("Inconsistent edge");
	}
	public int compareTo(Edge that){
		if (this.weight() < that.weight()) return -1;
		else if (this.weight() > that.weight()) return +1;
		else return 0;
	}
	public String toString(){ 
		return String.format("%d-%d %.2f", v, w, weight); 
	}
}
