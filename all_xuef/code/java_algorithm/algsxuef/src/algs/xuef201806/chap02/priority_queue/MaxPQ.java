package algs.xuef201806.chap02.priority_queue;

import algs.xuef201806.chap02.sort.SortBase;

/**
 * 基于完全二叉树的优先队列
 * @author moveb 
 * 20180609
 *
 */
public class MaxPQ<Key extends Comparable<Key>> {
	private Key[] pq;// pq[1..N]存储元素
	private int N;   //元素个数(同时也是尾元素下标)
	// 创建一个最大容量为 max 的优先队列
	public MaxPQ(int max){
		pq = (Key[]) new Comparable[max+1];
		N = 0;
	}
	/**
	 * 插入元素
	 * @param v
	 */
	public void insert(Key v){
		N++;
		// TODO 数组越界检查
		// 将新元素放在队列末尾
		pq[N] = v;
		// 上浮
		swim(N);
	}
	/**
	 * 删除并返回最大元素
	 * @return
	 */
	public Key deleteMax(){
		Key max = pq[1];
		pq[1] = pq[N];
		pq[N] = null;
		N--;
		sink(1);
		return max;
	}
	void sink(int i){
		while(i*2 <= N){
			// 找出i的两个孩子中最大的那个
			int j = i*2;
			if(j<N && SortBase.less(pq[j], pq[j+1])) j++;
			// 如果pq[i]比两个孩子都大,跳出循环
			if(!SortBase.less(pq[i], pq[j])) break;
			SortBase.exch(pq, i, j);
			i = j;
		}
	}
	void swim(int i){
		while(i/2 > 0 && SortBase.less(pq[i/2], i)){ // 如果比父节点大，就上浮
			SortBase.exch(pq, i/2, i);
			i = i/2;
		}
	}
}
