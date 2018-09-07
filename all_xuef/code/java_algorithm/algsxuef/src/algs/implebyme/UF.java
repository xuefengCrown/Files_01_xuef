package algs.implebyme;

import algs.base.StdIn;
import algs.base.StdOut;

public class UF {
	private int[] id; // access to component id (site indexed)
	
	private int count; // number of components
	public UF(int N)
	{ // Initialize component id array.
		count = N;
		id = new int[N];
		for (int i = 0; i < N; i++) id[i] = i;
	}
	public int count()
	{ return count; }
	public boolean connected(int p, int q)
	{ return find(p) == find(q); }
	public int find(int p){
		return id[p];
	}
	public void union(int p, int q){
		if(connected(p, q)) ;
		else{
			int temp=id[q];
			int temp2=id[p];
			for(int i=0; i<id.length; i++){
				if(id[i]==temp || id[i] == temp2) id[i]=temp;
			}
			count--;
		}
	}
	public static void main(String[] args)
	{ // Solve dynamic connectivity problem on StdIn.
		int N = StdIn.readInt(); // Read number of sites.
		UFquick uf = new UFquick(N); // Initialize N components.
		while (!StdIn.isEmpty())
		{
			int p = StdIn.readInt();
			int q = StdIn.readInt(); // Read pair to connect.
			//if (uf.connected(p, q)) continue; // Ignore if connected.
			uf.union(p, q); // Combine components
			//StdOut.println(p + " " + q); // and print connection.
		}
		StdOut.println(uf.count() + " components");
	}
}
