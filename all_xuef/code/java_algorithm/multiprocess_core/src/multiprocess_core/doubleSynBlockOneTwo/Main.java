package multiprocess_core.doubleSynBlockOneTwo;

public class Main {

	public static void main(String[] args) {
		ObjectService service = new ObjectService();
		
		ThreadA ta = new ThreadA(service);
		ta.setName("threadA");
		ThreadB tb = new ThreadB(service);
		tb.setName("threadB");
		ta.start();
		tb.start();
	}
}
