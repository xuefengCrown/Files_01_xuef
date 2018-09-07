package algs.implebyme;

import algs.base.Counter;
import algs.base.StdOut;

public class BinarySearch {
	public static void main(String[] args) {
		int key = 10;
		int[] a = {1, 6, 8, 10, 11, 13, 20, 31, 45, 61, 76, 90};
		Counter c = new Counter("keys");
		//StdOut.println(rank(key, a, 0, a.length - 1, 0));
		StdOut.println(rank2(key, a, c));
		StdOut.print("hit times: " + c.tally());
	}
	// 递归实现二分查找
	public static int rank(int key, int[] sortedArray, int start, int end, int recurDeepth){ //数组须升序排列
		int mid = (start + end)/2;
		for(int i=0; i<recurDeepth; i++) StdOut.print("*");
		StdOut.println("start-" + start + " end-" + end);
		if(key == sortedArray[mid]) return mid;
		else if(key > sortedArray[mid]) {
			recurDeepth++;
			return rank(key, sortedArray, mid, end, recurDeepth);
		}
		else {
			recurDeepth++;
			return rank(key, sortedArray, start, mid, recurDeepth);
		}
	}
	// 循环实现
	public static int rank2(int key, int[] a, Counter cou){
		int low = 0;
		int high = a.length - 1;
		while(low <= high){
			cou.increment();
			int mid = (low + high)/2;
			if(key == a[mid]) return mid;
			else if(key > a[mid]) low = mid + 1;
			else high = mid - 1;
		}
		return -1;
	}
}
