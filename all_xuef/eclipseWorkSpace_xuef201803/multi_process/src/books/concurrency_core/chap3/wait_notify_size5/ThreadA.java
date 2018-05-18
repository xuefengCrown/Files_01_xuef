package books.concurrency_core.chap3.wait_notify_size5;

public class ThreadA extends Thread {
	private Object lock;
	public ThreadA(Object lock) {
		this.lock = lock;
	}
	@Override
	public void run() {
		try {
			synchronized (lock) {
				if(MyList.size() != 5){
					System.out.println(Thread.currentThread().getName() + 
							" wait begin " + System.currentTimeMillis());
					// 当前线程等待。并释放被同步对象的锁。
					lock.wait();
					System.out.println(Thread.currentThread().getName() + 
							" wait end " + System.currentTimeMillis());
				}
			}
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
	}
}
