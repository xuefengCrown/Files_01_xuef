package algs.implebyme.efficiencyMeasure;

import algs.base.StdOut;
import algs.base.StdRandom;
// algorithms page 206
// 预测程序运行时间 倍率实验
public class DoublingRatio {
	public static double timeTrial(int N){
		int MAX = 1000000;
		int[] a = new int[N];
		for (int i = 0; i < N; i++)
			a[i] = StdRandom.uniform(-MAX, MAX);
		Stopwatch timer = new Stopwatch();
		//int cnt = ThreeSum.count(a);
		return timer.elapsedTime();
	}
	// same as for DoublingTest (page 177)
	public static void main(String[] args)
	{
		double prev = timeTrial(125);
		for (int N = 250; true; N += N)
		{
			double time = timeTrial(N);
			StdOut.printf("%6d %7.1f ", N, time);
			StdOut.printf("%5.1f\n", time/prev);
			prev = time;
		}
	}
}
