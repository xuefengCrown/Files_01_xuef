package algs.xuef201806.chap02.sort;

import algs.base.StdDraw;

/**
 * 插入排序；
 * 对于部分有序的数组特别有效
 * 1. 数组中每个元素距离它的最终位置都不远
 * 2. 一个有序的大数组接一个小数组
 * 3. 数组中只有几个元素的位置不正确
 * 
 * 改进：
 * 要大幅提高插入排序的速度并不难，只需要在内循环中将较大的元素
 * 都向右移动而并不总是交换两个元素（这样访问数组的次数就能减半）
 * 参见练习 2.1.25
 * @author moveb
 *
 */
public class Insertion extends SortBase {
	public static void sort(Comparable[] a){
		setXY();
		
		int N = a.length;
		// 至少要扫描完数组 a
		for(int i=0; i<N; i++){
			// 将a[i]插入到 a[0]...a[i-1],按照从小到大
			for(int j=i; j>0 && less(a[j], a[j-1]); j--){
				// 如果a[j]小于a[j-1],交换它们
				exch(a, j, j-1);
				//draw(a, j);
			}
		}
	}
	public static void sort_better(Comparable[] a){
		setXY();
		
		int N = a.length;
		// 至少要扫描完数组 a
		for(int i=0; i<N; i++){
			// 将a[i]插入到 a[0]...a[i-1],按照从小到大
			Comparable t = a[i];
			int j=i;
			for(; j>0 && less(t, a[j-1]); j--){
				// 如果a[j-1]比a[j]大，则把a[j-1] 右移
				
				a[j] = a[j-1];
			}
			// 找到了t的合适位置
			a[j] = t;
			//draw(a, j);
		}
	}
	
	// 初始化画板
	public static void setXY(){
		int N = 100;
		StdDraw.setXscale(0, N);
		StdDraw.setYscale(0, N);
		StdDraw.setPenRadius(.01);
		StdDraw.setPenColor(StdDraw.GRAY);
	}
}
