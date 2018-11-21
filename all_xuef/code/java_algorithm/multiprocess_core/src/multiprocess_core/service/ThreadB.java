package multiprocess_core.service;

public class ThreadB extends Thread {
	private HasSelfPrivateNum hspn;
	public ThreadB(HasSelfPrivateNum hspn){
		super();
		this.hspn = hspn;
	}
	
	@Override
	public void run(){
		super.run();
		this.hspn.addI("b");
	}
}
