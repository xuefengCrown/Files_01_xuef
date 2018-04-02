package multi_thread.thread;

public class Test2 {
	public static void main(String[] args) {
		Mythread2 thread = new Mythread2();
		// 多个线程共享数据
		Thread t1 = new Thread(thread, "A");
		Thread t2 = new Thread(thread, "B");
		Thread t3 = new Thread(thread, "C");
		Thread t4 = new Thread(thread, "C");
		Thread t5 = new Thread(thread, "C");
		t1.start();
		t2.start();
		t3.start();
		t4.start();
		t5.start();
	}
}
