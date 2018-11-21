package multiprocess_core.reEntrantLock;

public class Mian {

	public static void main(String[] args) {
		MyThread th = new MyThread();
		th.start();
	}
}
