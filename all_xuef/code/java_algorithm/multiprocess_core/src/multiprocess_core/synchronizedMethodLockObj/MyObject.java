package multiprocess_core.synchronizedMethodLockObj;

public class MyObject {

	synchronized
	public void mdA(){
		try {
			System.out.println("begin methodA threadName = " + Thread.currentThread().getName());
			Thread.sleep(5000);
			System.out.println("end");
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
	}
}
