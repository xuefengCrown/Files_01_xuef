package multiprocess_core.setNewStrTwoLock;

public class MyService {
	String lock= "123";
	
	public void testMethod(){
		try {
			synchronized (lock) {
				System.out.println(Thread.currentThread().getName() + " begin at " + 
						System.currentTimeMillis());
				lock = "456";
				Thread.sleep(2000);
				
				System.out.println(Thread.currentThread().getName() + " end at " + 
						System.currentTimeMillis());
			}
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
	}
}
