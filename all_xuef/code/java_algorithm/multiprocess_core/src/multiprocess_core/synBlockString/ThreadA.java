package multiprocess_core.synBlockString;

public class ThreadA extends Thread {
	Service service;
	public ThreadA(Service service){
		this.service = service;
	}
	
	@Override
	public void run(){
		service.setUnamePwd("A", "AA");
	}
}
