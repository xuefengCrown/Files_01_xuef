package algs.implebyme.sorting;

import java.util.NoSuchElementException;

public class IndexMaxPQ<Key extends Comparable<Key>> {
	private int n;           // number of elements on PQ
    private int[] pq;        // binary heap using 1-based indexing
    private int[] qp;        // inverse of pq - qp[pq[i]] = pq[qp[i]] = i
    private Key[] keys;      // keys[i] = priority of i
    public IndexMaxPQ(int maxN) {
        if (maxN < 0) throw new IllegalArgumentException();
        n = 0;
        keys = (Key[]) new Comparable[maxN + 1];    // make this of length maxN??
        pq   = new int[maxN + 1];
        qp   = new int[maxN + 1];                   // make this of length maxN??
        for (int i = 0; i <= maxN; i++)
            qp[i] = -1;
    }
    /**
     * Returns true if this priority queue is empty.
     *
     * @return {@code true} if this priority queue is empty;
     *         {@code false} otherwise
     */
    public boolean isEmpty() {
        return n == 0;
    }

    /**
     * Is {@code i} an index on this priority queue?
     * i key 的索引（存储在pq中）
     * @param  i an index
     * @return {@code true} if {@code i} is an index on this priority queue;
     *         {@code false} otherwise
     * @throws IllegalArgumentException unless {@code 0 <= i < maxN}
     */
    public boolean contains(int i) {
        return qp[i] != -1;
    }
    /**
     * Returns the number of keys on this priority queue.
     *
     * @return the number of keys on this priority queue 
     */
    public int size() {
        return n;
    }
    public void insert(int i, Key key) {
        if (contains(i)) throw new IllegalArgumentException("index is already in the priority queue");
        n++;
        qp[i] = n;
        pq[n] = i;
        keys[i] = key;
        swim(n);
    }
    public Key max(){
    	int max = pq[1];
    	return keys[pq[max]];
    }
    /**
     * Removes a maximum key and returns its associated index.
     *
     * @return an index associated with a maximum key
     * @throws NoSuchElementException if this priority queue is empty
     */
    public int delMax() {
        if (n == 0) throw new NoSuchElementException("Priority queue underflow");
        int min = pq[1];
        exch(1, n--);
        sink(1);

        assert pq[n+1] == min;
        qp[min] = -1;        // delete
        keys[min] = null;    // to help with garbage collection
        pq[n+1] = -1;        // not needed
        return min;
    }
    
    /***************************************************************************
     * Heap helper functions.
     ***************************************************************************/
     private void swim(int k) {
         while (k > 1 && less(k/2, k)) {
             exch(k, k/2);
             k = k/2;
         }
     }

     private void sink(int k) {
         while (2*k <= n) {
             int j = 2*k;
             if (j < n && less(j, j+1)) j++;
             if (!less(k, j)) break;
             exch(k, j);
             k = j;
         }
     }
     /***************************************************************************
      * General helper functions.
      ***************************************************************************/
      private boolean less(int i, int j) {
          return keys[pq[i]].compareTo(keys[pq[j]]) < 0;
      }

      private void exch(int i, int j) {
          int swap = pq[i];
          pq[i] = pq[j];
          pq[j] = swap;
          qp[pq[i]] = i;
          qp[pq[j]] = j;
      }
}
