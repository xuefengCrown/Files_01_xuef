package multiprocess_core.synchronizedMethodLockObj;

public class ThreadB extends Thread {
	private MyObject obj;
	public ThreadB(MyObject o){
		this.obj = o;
	}
	
	@Override
	public void run(){
		super.run();
		obj.mdA();
	}
}
