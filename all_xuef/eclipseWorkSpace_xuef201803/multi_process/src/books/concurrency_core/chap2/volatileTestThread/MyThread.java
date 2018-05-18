package books.concurrency_core.chap2.volatileTestThread;

public class MyThread extends Thread {
	/**
	 * volatile 本身并不处理数据的原子性，而是强制对数据的读写及时影响的主内存的。
	 */
	volatile public static int count;
	// 为 class 加锁
	synchronized private static void addCount(){
		for (int i = 0; i < 100; i++) {
			count++;
		}
		System.out.println("count=" + count);
	}
	@Override
	public void run() {
		addCount();
	}
}
