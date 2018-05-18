package books.concurrency_core.chap2.t9_volatile;

public class Run {
	public static void main(String[] args) {
		PrintString printStringService = new PrintString();
		printStringService.printStringMethod();
		// 主线程 main 在忙于执行 printStringMethod, 所以不会往下执行
		System.out.println("我要停止它! stopThread=" + Thread.currentThread().getName());
		printStringService.setContinuePrint(false);
	}
}
