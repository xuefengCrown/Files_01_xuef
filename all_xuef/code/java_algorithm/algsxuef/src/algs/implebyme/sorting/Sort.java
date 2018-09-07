package algs.implebyme.sorting;

import algs.base.StdDraw;
import algs.base.StdOut;

public class Sort {
	public static void sort(Comparable[] a)
	{ /* See Algorithms 2.1, 2.2, 2.3, 2.4, 2.5, or 2.7. */ }
	protected static boolean less(Comparable v, Comparable w)
	{ return v.compareTo(w) < 0; }
	protected static void exch(Comparable[] a, int i, int j)
	{ Comparable t = a[i]; a[i] = a[j]; a[j] = t; }
	protected static void show(Comparable[] a)
	{ // Print the array, on a single line.
		for (int i = 0; i < a.length; i++)
			StdOut.print(" "+a[i]);
		StdOut.println();
	}
	public static void setXY(){
		int N = 100;
		StdDraw.setXscale(0, N);
		StdDraw.setYscale(0, N);
		StdDraw.setPenRadius(.001);
		StdDraw.setPenColor(StdDraw.GRAY);
	}
	public static void draw(Comparable[] a, int g){
		setXY();
		StdDraw.clear();
		
		for (int i = 0; i < a.length; i++)
		{
			StdDraw.setPenColor(StdDraw.GRAY);
			if(i == g) StdDraw.setPenColor(StdDraw.BLACK);
			double halfH = ((Double) a[i])/10.0;
			double halfW = 50.0/(a.length+10);
			StdDraw.filledRectangle(2+ 4*i, 10+halfH, 0.8, halfH);
			//StdDraw.filledRectangle(x, y, halfWidth, halfHeight);
		}
	}
	public static boolean isSorted(Comparable[] a)
	{ // Test whether the array entries are in order.
		for (int i = 1; i < a.length; i++)
			if (less(a[i], a[i-1])) return false;
		return true;
	}
}
