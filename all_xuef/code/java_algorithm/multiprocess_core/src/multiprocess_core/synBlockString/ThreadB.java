package multiprocess_core.synBlockString;

public class ThreadB extends Thread {
	Service service;
	public ThreadB(Service service){
		this.service = service;
	}
	
	@Override
	public void run(){
		service.setUnamePwd("B", "BB");
	}
}
