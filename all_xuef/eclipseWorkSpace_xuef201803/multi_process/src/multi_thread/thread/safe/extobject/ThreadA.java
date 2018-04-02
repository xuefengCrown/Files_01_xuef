package multi_thread.thread.safe.extobject;

public class ThreadA extends Thread {
	private MyObject obj;

	public ThreadA(MyObject obj) {
		super();
		this.obj = obj;
	}
	@Override
	public void run(){
		super.run();
		obj.methodA();
	}
}
