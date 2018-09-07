package algs.xuef2018.priorityQueue;

import algs.base.StdOut;

/**
 * 随机进入，最大先出。广义队列之优先队列
 * @author moveb
 *
 */
public class MaxPQ<Key extends Comparable<Key>> {
	private Key[] pq; // store items at indices 1 to n
	private int N; // number of items on priority queue
	
	public MaxPQ(int capacity){
		pq = (Key[])new Comparable[capacity+1];
	}
	public boolean isEmpty(){
		return N==0;
	}
	public Key delMax(){
		Key max = pq[1];//Key x = pq[1]; // the name 'x' is not good
		pq[1] = pq[N];
		pq[N] = null;
		N--;
		sink(1);
		return max;
	}
	public void insert(Key key){
		N = N+1;
		pq[N] = key;
		swim(N);
	}
	public void swim(int k){
		while(k>1 && less(k/2, k)){
			exch(k/2, k);
			k = k/2;
		}
	}
	public void sink(int k){ //从k开始，一直下沉
		while(2*k <= N){
			int j = 2*k;
			if(j<N && less(j, j+1)){
				j = j+1;
			}
			if(!less(k, j)) break;
			exch(j, k);
			k = j;
		}
	}
	
	public boolean less(int i, int j){
		return pq[i].compareTo(pq[j]) < 0;
	}
	public void exch(int i, int j){
		Key temp = pq[i];
		pq[i] = pq[j];
		pq[j] = temp;
	}
}


