package algs.xuef201806.chap05.substring;

public class BoyerMoore {
	/**
	 * 各字符在pat中的索引(模式中最靠右的与之匹配的字符的索引)
	 * 如 pat = NEEDLE; 那么right[E]就是5
	 */
	private int[] right;
	private String pat;
	BoyerMoore(String pat){ 
		// Compute skip table.
		this.pat = pat;
		int M = pat.length();
		int R = 256;
		right = new int[R];
		// 初始化 right 数组
		for (int c = 0; c < R; c++)
			right[c] = -1; // -1 for chars not in pattern
		for (int j = 0; j < M; j++) // rightmost position for
			right[pat.charAt(j)] = j; // chars in pattern
	}
	/**
	 * 算法的基本框架还是暴力查找的框架
	 * 只是另外加上了灵活跳跃
	 * @param txt
	 * @return
	 */
	public int search(String txt){
		// Search for pattern in txt.
		int N = txt.length();
		int M = pat.length();
		/**
		 * i j 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
			   F I N D I N A H A Y  S  T  A  C  K  N  E  E  D  L  E  I  N  A
		   0 5 N E E D L E
		   5 5           N E E D L  E
		   11 4                        N  E  E  D  L  E
		   15 0                                    N  E  E  D  L  E
		 */
		int skip;
		for (int i = 0; i <= N-M; i += skip){ 
			// Does the pattern match the text at position i ?
			skip = 0;
			for (int j = M-1; j >= 0; j--)
				if (pat.charAt(j) != txt.charAt(i+j)){
					/**
					 * txt.charAt(i+j)为不匹配的字符;
					 * 1. 如果该字符存在于pat中,且在j的左面,那么 skip = j - right[txt.charAt(i+j)];
					 * 2. 如果该字符不在pat中, 那么 skip = j + 1; 也就是 skip = j - right[txt.charAt(i+j)];
					 * 3. 如果该字符存在于pat中,却在j的右面,那么 skip要调整为1;
					 * 这三种情况覆盖了所有情况
					 */
					skip = j - right[txt.charAt(i+j)]; // 适用于情况1,2
					if (skip < 1) skip = 1; // 适用于情况3
						break;
				}
			if (skip == 0) return i; // found.
		}
		return N; // not found.
	}
	public static void main(String[] args){
		// See page 769.
	}
}
