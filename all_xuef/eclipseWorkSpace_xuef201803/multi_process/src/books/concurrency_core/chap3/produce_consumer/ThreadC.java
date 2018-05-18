package books.concurrency_core.chap3.produce_consumer;

public class ThreadC extends Thread {
	private Consumer c;
	public ThreadC(Consumer c) {
		this.c = c;
	}
	@Override
	public void run() {
		while(true){
			c.getValue();
			try {
				Thread.sleep(2000);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}
	}
}
