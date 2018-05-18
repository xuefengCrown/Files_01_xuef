package books.concurrency_core.chap3.wait_notify_size5;

public class ThreadB extends Thread {
	private Object lock;

	public ThreadB(Object lock) {
		super();
		this.lock = lock;
	}
	@Override
	public void run() {
		try {
			synchronized (lock) {
				for(int i=0; i<10; i++){
					MyList.add();
					if(MyList.size() == 5){
						// 数量达到 5时，唤醒lock锁下的其他线程，
						// 但是要等此sync内的代码执行完，才释放锁lock
						/**
						 * notify 操作可以唤醒一个因调用了wait操作而处于阻塞状态中的线程，使其进入就绪状态
						 */
						lock.notify(); // 并不立即释放锁
						System.out.println("已发出通知");
					}
					System.out.println("添加了 " + (i+1) + " 个元素");
					Thread.sleep(1000);
				}
			}
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
	}
}
