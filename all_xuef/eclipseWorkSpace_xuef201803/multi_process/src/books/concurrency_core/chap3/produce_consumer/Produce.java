package books.concurrency_core.chap3.produce_consumer;
// 生产者
public class Produce {
	private String lock;
	public Produce(String lock){
		super();
		this.lock = lock;
	}
	public void setValue(){
		try{
			synchronized (lock) {
				/**
				 * ValueObject 中有非空值时就等待；没有时就生产
				 */
				if(!ValueObject.value.equals("")){
					lock.wait();
				}
				String value = System.currentTimeMillis() + "_" + System.nanoTime();
				System.out.println("set 的值是 " + value);
				ValueObject.value = value;
				lock.notify();
			}
		} catch(InterruptedException e){
			
		}
	}
}
