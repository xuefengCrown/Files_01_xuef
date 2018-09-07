package algs.xuef201806.chap02.priority_queue;

public class TestMaxPQ {
	public static void main(String[] args) {
		MaxPQ<Integer> pq = new MaxPQ(20);
		pq.insert(10);
		pq.insert(1);
		pq.insert(9);
		pq.insert(7);
		System.out.println(pq.deleteMax());
		System.out.println(pq.deleteMax());
		System.out.println(pq.deleteMax());
		System.out.println(pq.deleteMax());
	}
}
