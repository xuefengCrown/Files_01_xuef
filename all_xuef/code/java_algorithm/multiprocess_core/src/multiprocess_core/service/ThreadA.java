package multiprocess_core.service;

public class ThreadA extends Thread {
	private HasSelfPrivateNum hspn;
	public ThreadA(HasSelfPrivateNum hspn){
		super();
		this.hspn = hspn;
	}
	
	@Override
	public void run(){
		super.run();
		this.hspn.addI("a");
	}
}
