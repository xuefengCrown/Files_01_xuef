package multi_thread.thread;

public class Mythread1 extends Thread {
	int count;
	
	public Mythread1(int count, String name){
		super();
		this.count = count;
		this.setName(name);
	}

	@Override
	public void run() {
		super.run();
		while(count > 0){
			count--;
			System.out.println(this.currentThread().getName() + 
					": count = " + count);
		}
	}
	
}
