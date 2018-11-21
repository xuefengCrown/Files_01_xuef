package multiprocess_core.reEntrantLock;

public class MyThread extends Thread {

	@Override
	public void run(){
		Service service  = new Service();
		service.service1();
	}
}
