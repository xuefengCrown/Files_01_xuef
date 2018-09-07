package algs.implebyme.exercise1;

import algs.base.StdOut;
import algs.base.StdRandom;

public class Exercise_1_35_Dice_simulation {

	public static void main(String[] args) {
		double[] res = formuladice();
		int N = 10000;
		while(!satisfied(res, diceSimulation(N)))
			N+=1000;
		StdOut.print(N);
	}
	public static boolean satisfied(double[] res, double[] simu){
		double precision = 0.0009;
		for(int i=2; i<res.length; i++){
			if(Math.abs(res[i]-simu[i])>precision) return false;
		}
		for(int i=2; i<res.length; i++){
			StdOut.printf("%7.4f",res[i]);
			StdOut.printf("%7.4f",simu[i]);
			StdOut.println();
		}
		return true;
	}
	public static double[] diceSimulation(int N){
		int s = 6;
		double[] dist = new double[2*s+1];
		for(int i=0; i<N; i++){
			dist[StdRandom.uniform(1, 7)+StdRandom.uniform(1, 7)]++;
		}
		for(int i=2; i<=2*s; i++){
			//StdOut.println(i+ "---"+ (dist[i] /= (N*1.0)));
			dist[i] /= (N*1.0);
		}
		return dist;
	}
	public static double[] formuladice(){
		int SIDES = 6;
		double[] dist = new double[2*SIDES+1];
		for (int i = 1; i <= SIDES; i++)
			for (int j = 1; j <= SIDES; j++)
				dist[i+j] += 1.0;
		for (int k = 2; k <= 2*SIDES; k++)
			dist[k] /= 36.0;
		return dist;
	}
}
