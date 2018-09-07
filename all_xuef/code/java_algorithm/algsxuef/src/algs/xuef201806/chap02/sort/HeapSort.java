package algs.xuef201806.chap02.sort;

import algs.base.StdDraw;

public class HeapSort {
	public static void sort(Comparable[] a){
		// 画板初始化
		setXY();
		// a[0]不使用,所以N = a.length-1
		int N = a.length-1;
		// 构造堆
		for(int k=N/2; k>=1; k--){
			sink(a, k, N);
		}
		/**
		 * 将堆的最大元素a[1]与堆尾元素a[N]交换;
		 * sink(1) 以得到有序堆;
		 */
		while(N>=1){
			exch(a, 1, N--);
			sink(a, 1, N);
		}
		// 此时, a[1]~a[N] 是有序的;(升序)
	}
	// 初始化画板
	public static void setXY(){
		int N = 100;
		StdDraw.setXscale(0, N);
		StdDraw.setYscale(0, N);
		StdDraw.setPenRadius(.01);
		StdDraw.setPenColor(StdDraw.GRAY);
	}
	static void sink(Comparable[] pq, int i, int N){
		
		while(i*2 <= N){
			// 找出i的两个孩子中最大的那个
			int j = i*2;
			if(j<N && less(pq[j], pq[j+1])) j++;
			// 如果pq[i]比两个孩子都大,跳出循环
			if(!less(pq[i], pq[j])) break;
			exch(pq, i, j);
			//???
			draw(pq, i, i, j);
			i = j;
		}
		draw(pq);
	}
	static void swim(Comparable[] pq, int i, int N){
		while(i/2 > 0 && less(pq[i/2], i)){ // 如果比父节点大，就上浮
			exch(pq, i/2, i);
			i = i/2;
		}
	}
	
	public static boolean less(Comparable v, Comparable w){
		return v.compareTo(w) < 0;
	}
	// 交换 a[i] a[j]
	public static void exch(Comparable[] a, int i, int j){
		Comparable temp = a[i];
		a[i] = a[j];
		a[j] = temp;
		// 黑色的元素正在进行交换
		//draw(a, i, i, j);
	}
	/**
	 * @param a
	 * @param sink 正在下沉的元素
	 * @param swapA 在交换的元素
	 * @param swapB
	 */
	public static void draw(Comparable[] a, int sink, int swapA, int swapB){
		StdDraw.clear();
		
		int N = a.length;
		for(int i=0; i<N; i++){
			StdDraw.setPenColor(StdDraw.GRAY);
			if(i == swapA || i == swapB) StdDraw.setPenColor(StdDraw.BLACK);
			if(i == sink) StdDraw.setPenColor(StdDraw.RED);
			double x = 2.0*i;
			double y = (Integer)a[i]/2.0;
			double rw = 8.0/N;
			double rh = (Integer)a[i]/2.0;
			
			StdDraw.filledRectangle(x, y, rw, rh);
		}
		/**
		try {
			Thread.sleep(200);
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
		*/
	}
	
	public static void draw(Comparable[] a, int swapA, int swapB){
		StdDraw.clear();
		
		int N = a.length;
		for(int i=0; i<N; i++){
			StdDraw.setPenColor(StdDraw.GRAY);
			if(i == swapA || i == swapB) StdDraw.setPenColor(StdDraw.BLACK);
			
			double x = 2.0*i;
			double y = (Integer)a[i]/2.0;
			double rw = 8.0/N;
			double rh = (Integer)a[i]/2.0;
			
			StdDraw.filledRectangle(x, y, rw, rh);
		}
	}
	public static void draw(Comparable[] a){
		StdDraw.clear();
		
		int N = a.length;
		for(int i=0; i<N; i++){
			StdDraw.setPenColor(StdDraw.GRAY);
			//if(i == tar) StdDraw.setPenColor(StdDraw.RED);
			
			double x = 2.0*i;
			double y = (Integer)a[i]/2.0;
			double rw = 8.0/N;
			double rh = (Integer)a[i]/2.0;
			
			StdDraw.filledRectangle(x, y, rw, rh);
		}
	}
}
