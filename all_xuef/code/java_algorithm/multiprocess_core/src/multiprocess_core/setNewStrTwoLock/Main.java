package multiprocess_core.setNewStrTwoLock;

public class Main {

	public static void main(String[] args) throws InterruptedException {
		MyService s = new MyService();
		ThreadA ta = new ThreadA(s);
		ta.setName("A");
		ThreadB tb = new ThreadB(s);
		tb.setName("B");
		ta.start();
		Thread.sleep(50); // main thread sleep
		tb.start();
	}
}
