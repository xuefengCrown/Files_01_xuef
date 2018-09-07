package algs.implebyme.exercise1;

import algs.base.In;

public class Exercise1_32 {

	public static void main(String[] args) {
		int N = 50;
		double l = 1.6;
		double r = 9.8;
		double[] doubleList = In.readDoubles(args[0]);
		
	}
	public static void drawRec(int n, double l, double r, double[] dL){
		double w = (r-l)/n;
		int[] counters = new int[n];
		for(int i=0; i<n; i++) counters[i]=0;
		for(int i=0; i<dL.length; i++){
			int k = getInterval(dL[i], n, l, r);
            if (k >= 0)
                counters[k]++;
		}
	}
	private static int getInterval(double v, int n, double l, double r)
    {
        if (v < l || v >= r)
            return -1;
        else
            return (int)(n * (v - l) / (r - l));
    }
}
