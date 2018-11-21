package multiprocess_core.dirtyRead;

/**
 * 因为getValue未同步，导致脏读
 * @author moveb
 *
 */
public class PublicVar {
	public String uname = "A";
	public String pwd = "AA";
	
	synchronized
	public void setValue(String u, String p){
		try {
			this.uname = u;
			Thread.sleep(5000);
			this.pwd = p;
			System.out.println("setValue mathod thread name=" + Thread.currentThread().getName()
					+ " ,username = " + uname + " password = " + pwd);
			
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
	}
	
	synchronized
	public void getValue(){
		System.out.println("getValue mathod thread name=" + Thread.currentThread().getName()
				+ " ,username = " + uname + " password = " + pwd);
	}
}
