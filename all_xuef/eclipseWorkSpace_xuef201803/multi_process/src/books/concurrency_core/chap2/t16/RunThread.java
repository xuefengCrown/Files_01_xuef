package books.concurrency_core.chap2.t16;

public class RunThread extends Thread {
	/**
	 * volatile
	 * 主要作用就是当线程访问isRunning 这个变量时，强制性从公共堆栈中取值
	 */
	volatile private boolean isRunning = true;
	
	public boolean isRunning() {
		return isRunning;
	}
	public void setRunning(boolean isRunning) {
		this.isRunning = isRunning;
	}
	@Override
	public void run() {
		System.out.println("进入 run 了");
		while(isRunning){
			
		}
		System.out.println("线程被停止了！");
	}
}
