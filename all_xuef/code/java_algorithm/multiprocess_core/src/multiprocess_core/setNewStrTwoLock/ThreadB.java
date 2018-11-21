package multiprocess_core.setNewStrTwoLock;

public class ThreadB extends Thread {

	MyService service;
	public ThreadB(MyService service){
		this.service = service;
	}
	
	@Override
	public void run(){
		super.run();
		service.testMethod();
	}
}
