/**
 *  编译：
 *  执行：
 *  所依赖的库：StdOut.java
 *  简介：找出最大元素的优先队列，使用二叉堆实现（以数组表示的完全二叉树作为data stru）
 *  ---------------------------------------------------------------------------
 *	Compilation:  javac MaxPQ_byheap.java
 *  Execution:    java MaxPQ_byheap
 *  Dependencies: StdOut.java
 *
 *  Maximum-oriented PQ implementation using a binary heap(complete binary tree).
 */
package algs.implebyme.sorting;

import java.util.NoSuchElementException;

import algs.base.StdIn;
import algs.base.StdOut;
import algs.base.StdRandom;
/**
 *  类的介绍：找出最大元素的优先队列，使用数组表示的完全二叉树来表征二叉堆。
 *  方法：insert-插入元素；delMax-return当前队列中的最大元素。
 *  实现细节：...
 *  时间复杂度：...
 *  空间复杂度：...
 *  更多细节导航：
 *  作者：@author yourname 2017.8.10
 *  泛型 接口的说明：...
 *  --------------------------------------------------------------------
 *  The {@code MaxPQ_byheap} class represents ...
 *  It supports the usual <em>insert</em> and <em>delMax</em> operations.
 *  In order to let the client refer to ...
 *  
 *  It also supports methods for ...
 *  
 *  This implementation uses ...
 *  
 *  The <em>insert</em>, <em>delMax</em> operations take logarithmic time.
 *  Construction takes time proportional to the specified capacity.
 *  <p>
 *  For additional documentation, see <a href="http://algs4.cs.princeton.edu/24pq">Section 2.4</a> of
 *  <i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne.
 *
 *  @author Robert Sedgewick
 *  @author Kevin Wayne
 *
 *  @param <Key> the generic type of key on this priority queue
 */
public class MaxPQ_byheap<Key extends Comparable<Key>> {//??
	private Key[] pq; //heap-ordered complete binary tree(not use pq[0])
	private int N = 0; //number of items on priority queue
	/**
	 * Initializes an empty priority queue with the given initial capacity.(方法功能intro)
	 * @param maxN the initial capacity of this priority queue(参数说明) 
	 */
	public MaxPQ_byheap(int maxN){ 
		pq = (Key[]) new Comparable[maxN+1]; 
	}
	/**
	 * Returns true if this priority queue is empty.
	 * @return {@code true} if this priority queue is empty;
     *         {@code false} otherwise
	 */
	public boolean isEmpty()
	{ 
		return N == 0; 
	}
	/**
	 * Returns the number of items on the pq
	 * @return
	 */
	public int size()
	{ 
		return N; 
	}
	/**
	 * Adds a new key to this priority queue.
     * @param v the new key to add to this priority queue
	 */
	public void insert(Key v)
	{
		N++;
		pq[N] = v;
		swim(N);
	}
	/**
	 * Returns and delete a largest key on this priority queue.
	 * @return
	 * @throws NoSuchElementException if this priority queue is empty
	 */
	public Key delMax()
	{
		if (isEmpty()) throw new NoSuchElementException("Priority queue underflow");
		Key max = pq[1]; // Retrieve max key from top.
		exch(1, N--); // Exchange with last item.
		pq[N+1] = null; // Avoid loitering.
		sink(1); // Restore heap property.
		return max;
	}
	/***************************************************************************
	    * Helper functions for compares and swaps.
	    ***************************************************************************/
	private boolean less(int i, int j){
		return pq[i].compareTo(pq[j])<0;
	}
	private void exch(int i, int j){
		Key t = pq[i]; 
		pq[i] = pq[j]; 
		pq[j] = t;
	}
	/***************************************************************************
	    * Helper functions to restore the heap invariant.
	    ***************************************************************************/
	private void swim(int k){
		while (k > 1 && less(k/2, k))
		{
			exch(k/2, k);
			k = k/2;
		}
	}
	private void sink(int k){
		while (2*k <= N)
		{
			int j = 2*k;
			if (j < N && less(j, j+1)) j++;
			if (!less(k, j)) break;
			exch(k, j);
			k = j;
		}
	}
	// test
	public static void main(String[] args) {
		MaxPQ_byheap<Character> maxpq = new MaxPQ_byheap<>(30);
		
		while(!StdIn.isEmpty()){
			maxpq.insert(StdIn.readChar());
		}
		while(!maxpq.isEmpty()){
			StdOut.print(" "+maxpq.delMax());
		}
	}
}
