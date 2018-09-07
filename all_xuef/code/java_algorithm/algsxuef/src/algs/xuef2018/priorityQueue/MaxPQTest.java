package algs.xuef2018.priorityQueue;

import algs.base.StdOut;

public class MaxPQTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		MaxPQ pq = new MaxPQ<Integer>(5);
		pq.insert(1);
		pq.insert(2);
		pq.insert(8);
		pq.insert(16);
		StdOut.print(pq.delMax());
		StdOut.print(pq.delMax());
		StdOut.print(pq.delMax());
	}

}
