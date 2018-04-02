package multi_thread.thread.safe.dirtRead;

public class PublicVar {
	public String username = "A";
	public String password = "AA";
	
	synchronized public void setValue(String u, String p) {
		try {
			this.username = u;
			Thread.sleep(5000);
			this.password = p;
			System.out.println("setValue method thread-name: " + 
						Thread.currentThread().getName() + 
						"username = " + username + " password = " + 
						password);
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
	}
	public void getValue(){
		System.out.println("getValue method thread-name: " + 
				Thread.currentThread().getName() + 
				"username = " + username + " password = " + 
				password);
	}
}
