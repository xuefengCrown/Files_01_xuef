package multiprocess_core.doubleSynBlockOneTwo;

public class ThreadB extends Thread {

	ObjectService os;
	public ThreadB(ObjectService os){
		this.os = os;
	}
	
	@Override
	public void run(){
		os.serviceMethodB();
	}
}
