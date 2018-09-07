package algs.xuef201806.chap05.substring;
/**
 * ±©Á¦²éÕÒ×Ó´®
 * @author moveb
 *
 */
public class BruteForce {
	/**
	 * pat-->N E E D L E
	   txt-->I N A H A Y S T A C K N E E D L E I N A
	 * @param pat
	 * @param txt
	 * @return
	 */
	public static int search(String pat, String txt){
		int M = pat.length();
		int N = txt.length();
		for (int i = 0; i <= N - M; i++){
			int j;
			for (j = 0; j < M; j++)
				if (txt.charAt(i+j) != pat.charAt(j))
					break;
			if (j == M) return i; // found
		}
		return N; // not found
	}
}
