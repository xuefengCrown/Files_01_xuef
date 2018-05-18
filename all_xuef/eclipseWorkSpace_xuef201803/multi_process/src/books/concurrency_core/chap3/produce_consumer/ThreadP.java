package books.concurrency_core.chap3.produce_consumer;

public class ThreadP extends Thread {
	private Produce p;
	public ThreadP(Produce p) {
		this.p = p;
	}
	@Override
	public void run() {
		while(true){
			p.setValue();
			try {
				Thread.sleep(2000);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}
	}
}
