package multi_thread.thread.safe.dirtRead;

public class ThreadA extends Thread {
	public PublicVar pv;

	public ThreadA(PublicVar pv) {
		super();
		this.pv = pv;
	}

	@Override
	public void run() {
		super.run();
		pv.setValue("B", "BB");
	}
	
}
