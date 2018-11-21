package multiprocess_core.doubleSynBlockOneTwo;

public class ThreadA extends Thread {

	ObjectService os;
	public ThreadA(ObjectService os){
		this.os = os;
	}
	
	@Override
	public void run(){
		os.serviceMethodA();
	}
}
