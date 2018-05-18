package books.concurrency_core.chap3.twoThreadTransData;

public class ThreadA extends Thread {
	private MyList list;
	public ThreadA(MyList list) {
		this.list = list;
	}
	
	@Override
	public void run() {
		try {
			for(int i=0; i<10; i++){
				list.add();
				System.out.println("add " + (i+1) + " elements");
				Thread.sleep(1000);
			}
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
	}
}
