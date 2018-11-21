package multiprocess_core.synBlockString;

public class Main {

	public static void main(String[] args) {
		Service service = new Service();
		
		ThreadA ta = new ThreadA(service);
		ta.setName("threadA");
		ThreadB tb = new ThreadB(service);
		tb.setName("threadB");
		ta.start();
		tb.start();
	}
}
