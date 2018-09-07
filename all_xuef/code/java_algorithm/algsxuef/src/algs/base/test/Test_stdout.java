package algs.base.test;

import algs.base.StdDraw;
import algs.base.StdOut;

public class Test_stdout {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		/*
		StdOut.print("im the best");
		int N = 100;
		StdDraw.setXscale(0, N);
		StdDraw.setYscale(0, N*N);
		StdDraw.setPenRadius(.01);
		for (int i = 1; i <= N; i++)
		{
			StdDraw.point(i, i);
			StdDraw.point(i, i*i);
			StdDraw.point(i, i*Math.log(i));
		}
		*/
		String string1 = "hello";
		String string2 = string1;
		string1 = "world";
		StdOut.println(string1);
		StdOut.println(string2);
	}

}
