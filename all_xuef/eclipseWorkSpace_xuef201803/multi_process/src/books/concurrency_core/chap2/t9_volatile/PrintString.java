package books.concurrency_core.chap2.t9_volatile;

public class PrintString {
	private boolean isContinuePrint = true;
	public boolean isContinuePrint() {
		return isContinuePrint;
	}
	public void setContinuePrint(boolean isContinuePrint) {
		this.isContinuePrint = isContinuePrint;
	}
	public void printStringMethod() {
		try {
			while(isContinuePrint){
				System.out.println("run printStringMethod threadName=" 
											+ Thread.currentThread().getName());
				Thread.sleep(1000);
			}
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
	}
}
