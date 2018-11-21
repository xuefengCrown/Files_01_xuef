package multiprocess_core.dirtyRead;

public class Main {
	public static void main(String[] args) {
		try {
			PublicVar pv = new PublicVar();
			ThreadA ta = new ThreadA(pv);
			ta.start(); // setValue in ta Thread
			Thread.sleep(200);
			pv.getValue();
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
	}
}
