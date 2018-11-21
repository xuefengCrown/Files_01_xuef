package multiprocess_core.dirtyRead;

public class ThreadA extends Thread {

	PublicVar pv;
	public ThreadA(PublicVar pv){
		super();
		this.pv = pv;
	}
	
	@Override
	public void run(){
		super.run();
		pv.setValue("B", "BB");
	}
}
