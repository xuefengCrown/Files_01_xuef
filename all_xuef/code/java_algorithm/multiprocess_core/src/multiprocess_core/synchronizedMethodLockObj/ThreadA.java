package multiprocess_core.synchronizedMethodLockObj;

public class ThreadA extends Thread {
	private MyObject obj;
	public ThreadA(MyObject o){
		this.obj = o;
	}
	
	@Override
	public void run(){
		super.run();
		obj.mdA();
	}
}
