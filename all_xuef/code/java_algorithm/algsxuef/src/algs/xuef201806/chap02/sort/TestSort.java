package algs.xuef201806.chap02.sort;

import algs.base.StdOut;
import algs.base.StdRandom;

public class TestSort {
	public static void main(String[] args) {
		Integer[] a = new Integer[50];
		for(int i=0; i<a.length; i++){
			a[i] = StdRandom.uniform(100);
		}
		SortBase.show(a);
		//Insertion.sort(a);
		Merge.sort(a);
		StdOut.println("\n-----------------------");
		SortBase.show(a);
	}
}
