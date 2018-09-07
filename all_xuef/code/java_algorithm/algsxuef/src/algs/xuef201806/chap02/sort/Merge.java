package algs.xuef201806.chap02.sort;

import algs.base.StdDraw;

/**
 * 自顶向下的归并排序
 * 归并排序对于理解递归思想和分治思想很有帮助
 * 
 * 改进：
 * 1. 使用插入排序处理小规模的子数组（比如长度小于15）,
 * 	     一般能够将归并排序的运行时间缩短10%-15%
 * 2. 测试数组是否有序！
 * 	  我们可以添加一个判断条件,如果a[mid]小于a[mid+1],那么说明数组已经有序并跳过merge方法。
 * 
 * @author moveb
 *
 */
public class Merge extends SortBase {
	// 归并所需的辅助数组
	private static Comparable[] aux;
	public static void sort(Comparable[] a){
		aux = new Comparable[a.length];
		sort(a, 0, a.length-1);
	}
	public static void sort(Comparable[] a, int lo, int hi){
		setXY();
		
		// 单元素是有序的
		if(lo >= hi) return;
		int mid = lo + (hi-lo)/2;
		// 排序左半边
		sort(a, lo, mid);
		// 排序右半边
		sort(a, mid+1, hi);
		// 归并
		merge(a, lo, mid, hi);
		draw(a);
	}
	/**
	 * 对以mid为界(左右半边都是分别有序的)的数组a进行原地归并
	 * mid: 左半边尾部元素的下标
	 */
	public static void merge(Comparable[] a, int lo, int mid, int hi){
		int i = lo, j = mid + 1;
		// ??? a.clone()到底做了什么
		// 辅助数组 
		// Comparable[] aux = a.clone();
		
		for(int k=lo; k<=hi; k++){
			aux[k] = a[k];
		}
		
		/**
		 * 左半边，右半边各一根指针；向右扫描
		 */
		for(int k=lo; k<=hi; k++){
			if(i > mid)  		// 左半边用尽
				a[k] = aux[j++];
			else if(j > hi)		// 右半边用尽
				a[k] = aux[i++];
			else if(less(aux[j], aux[i]))
				a[k] = aux[j++];
			else
				a[k] = aux[i++];
		}
	}
	/**
	 * 废弃
	 * 仅为了说明如何调用 merge
	 * @param args
	 */
	public static void main(String[] args) {
		Integer[] a = new Integer[]{1,3,7,18, 2, 4, 5, 6, 15};
		merge(a, 0, 3, a.length-1);
		show(a);
	}
	
	public static void setXY(){
		int N = 100;
		StdDraw.setXscale(0, N);
		StdDraw.setYscale(0, N);
		StdDraw.setPenRadius(.01);
		StdDraw.setPenColor(StdDraw.GRAY);
	}
}
