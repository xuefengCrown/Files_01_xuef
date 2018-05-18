package books.concurrency_core.chap3.produce_consumer;
// 消费者
public class Consumer {
	private String lock;
	public Consumer(String lock) {
		this.lock = lock;
	}
	public void getValue(){
		try {
			synchronized (lock) {
				if(ValueObject.value.equals("")){
					lock.wait();
				}
				System.out.println("get 的值是 " + ValueObject.value);
				ValueObject.value = "";
				lock.notify();
			}
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
	}
}
