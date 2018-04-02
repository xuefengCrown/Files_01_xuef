package multi_thread.thread;

public class Test1 {
	public static void main(String[] args) {
		Thread t1 = new Mythread1(5, "thread 1");
		Thread t2 = new Mythread1(5, "thread 2");
		Thread t3 = new Mythread1(5, "thread 3");
		
		t1.start();
		t2.start();
		t3.start();
	}
}
