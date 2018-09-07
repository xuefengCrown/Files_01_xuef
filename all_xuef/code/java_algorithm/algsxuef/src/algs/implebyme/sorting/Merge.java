package algs.implebyme.sorting;
// 分治思想的最典型例子

public class Merge extends Sort {
	private static Comparable[] aux; // auxiliary array for merges
	public static void sort(Comparable[] a)
	{
		aux = new Comparable[a.length]; // Allocate space just once.
		sort(a, 0, a.length - 1);
	}
	private static void sort(Comparable[] a, int lo, int hi)
	{ // Sort a[lo..hi].
		if (hi <= lo) return;
		int mid = lo + (hi - lo)/2;
		sort(a, lo, mid); // Sort left half.
		sort(a, mid+1, hi); // Sort right half.
		merge(a, lo, mid, hi); // Merge results (code on page 271).
	}
	// 数组a 左半有序（升序） 右半有序（升序）；  如何merge 达到全体升序
	public static void merge(Comparable[] a, int lo, int mid, int hi){
		// Merge a[lo..mid] with a[mid+1..hi].
		int i = lo, j = mid+1;
		for (int k = lo; k <= hi; k++) // Copy a[lo..hi] to aux[lo..hi].
			aux[k] = a[k];
		for (int k = lo; k <= hi; k++) // Merge back to a[lo..hi].
			if (i > mid) a[k] = aux[j++];
			else if (j > hi ) a[k] = aux[i++];
			else if (less(aux[j], aux[i])) a[k] = aux[j++];
			else a[k] = aux[i++];;

	}
	
	public static void main(String[] args) {
		Integer[] a = {1, 4, 7, 2, 6, 8, 17, 89};
		merge(a, 0, 2, 7);
		show(a);
	}
}
