package multi_thread.thread.safe.extobject;

public class MyObject {
	synchronized public void methodA(){
		try {
			System.out.println("begin mathodA thread-name: " +
						Thread.currentThread().getName());
		
			Thread.sleep(5000);
			System.out.println("end...");
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
	}
	
	synchronized public void methodB(){
		try {
			System.out.println("begin mathodB thread-name: " +
						Thread.currentThread().getName());
		
			Thread.sleep(5000);
			System.out.println("end...");
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
	}
}
