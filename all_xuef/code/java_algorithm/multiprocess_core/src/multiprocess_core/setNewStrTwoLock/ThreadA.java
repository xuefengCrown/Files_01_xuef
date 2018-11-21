package multiprocess_core.setNewStrTwoLock;

public class ThreadA extends Thread {

	MyService service;
	public ThreadA(MyService service){
		this.service = service;
	}
	
	@Override
	public void run(){
		super.run();
		service.testMethod();
	}
}
