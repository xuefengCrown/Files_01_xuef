package books.concurrency_core.chap2.syncUpdateNewValue;

public class Service {
	private boolean isContinueRun = true;
	public void runMethod(){
		String anyS = new String();
		while(isContinueRun){
//			synchronized (anyS) {
//				
//			}
		}
		System.out.println("Õ£œ¬¿¥¡À...");
	}
	public void stopMethod(){
		isContinueRun = false;
	}
}
