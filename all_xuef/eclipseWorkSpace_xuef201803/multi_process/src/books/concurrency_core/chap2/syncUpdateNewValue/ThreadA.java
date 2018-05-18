package books.concurrency_core.chap2.syncUpdateNewValue;

public class ThreadA extends Thread {
	private Service service;
	public ThreadA(Service service) {
		this.service = service;
	}
	@Override
	public void run() {
		service.runMethod();
	}
}
