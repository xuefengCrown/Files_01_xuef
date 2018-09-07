package algs.implebyme.exercise1;

import algs.base.StdOut;

public class Ex1_2_6_circular_rotation {
	public static void main(String[] args) {
		//isCircularRotation("ACTGACG", "TGACGAC");
		StdOut.print(mystery("helloworld"));
	}
	public static boolean isCircularRotation(String s, String t){
		StdOut.println(t.substring(1));
		//(s.length() == t.length()) && (s.concat(s).indexOf(t) >= 0)
		StdOut.println(t.substring(1).concat(t.substring(0, 1)));
		t=t.substring(1).concat(t.substring(0, 1));
		StdOut.print(t.substring(1).concat(t.substring(0, 1)));
		return false;
	}
	public static String mystery(String s)
	{
		int N = s.length();
		if (N <= 1) return s;
		String a = s.substring(0, N/2);
		String b = s.substring(N/2, N);
		return mystery(b) + mystery(a);
	}
}
