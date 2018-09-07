package algs.xuef201806.chap04;

public class Degree implements Comparable<Degree> {
	private int idx;
	private int degrees;
	public Degree(int i, int d){
		idx = i;
		degrees = d;
	}
	@Override
	public int compareTo(Degree other) {
		if(this.degrees < other.degrees) return -1;
		else if(this.degrees > other.degrees) return 1;
		else{
			if(this.idx < other.idx) return -1;
			else if(this.idx > other.idx) return 1;
			else return 0;
		}
	}
	
	public int getIdx() {
		return idx;
	}
	public void setIdx(int idx) {
		this.idx = idx;
	}
	public int getDegrees() {
		return degrees;
	}
	public void setDegrees(int degrees) {
		this.degrees = degrees;
	}
	@Override
	public String toString() {
		return "Degree [idx=" + idx + ", degrees=" + degrees + "]";
	}
}
