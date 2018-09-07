package algs.implebyme.sorting;

import algs.base.StdOut;

// quick sort version1
public class Quick extends Sort{
	public static void sort(Comparable[] a)
	{
		//StdRandom.shuffle(a); // Eliminate dependence on input.
		sort(a, 0, a.length - 1);
	}
	public static void sort(Comparable[] a, int low, int high){
		if (high <= low) return;
		int j = partition(a, low, high); // Partition (see page 291).
		sort(a, low, j-1); // Sort left part a[lo .. j-1].
		sort(a, j+1, high); // Sort right part a[j+1 .. hi].
	}
	// 切分 ; return 主元(pivot)切分后的确定位置；
	// 这里每一轮切分，都以a[low]作为主元（待改进）
	public static int partition(Comparable[] a, int low, int high){
		Comparable pivot = a[low];
		int i = low;
		int j = high+1;
		while(true){
			// 从左向右扫瞄，直到有a[i] 大于主元
			while(less(a[++i], pivot)) if(i==high) break;
			// 从右向左扫瞄，直到有a[j] 小于主元
			while(less(pivot, a[--j])) if(low==j) break;
			if(i>=j) break;
			exch(a, i, j);
		}
		exch(a, j, low);
		return j;
	}
	public static void main(String[] args) {
		Integer[] arr = {7, 1, 9, 15, 3, 8, 6, 2, 16, 10, 4, 11, 5};
		sort(arr);
		Sort.show(arr);
	}
}
