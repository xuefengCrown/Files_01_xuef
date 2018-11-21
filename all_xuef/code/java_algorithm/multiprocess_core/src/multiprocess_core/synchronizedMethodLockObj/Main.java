package multiprocess_core.synchronizedMethodLockObj;

public class Main {
	public static void main(String[] args) {
		MyObject o = new MyObject();
		ThreadA aTh = new ThreadA(o);
		ThreadB bTh = new ThreadB(o);
		aTh.setName("A");
		bTh.setName("B");
		aTh.start();
		bTh.start();
	}
}
