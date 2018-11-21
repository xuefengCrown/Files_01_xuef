package multiprocess_core.synBlockString;

public class Service {
	String uname;
	String pwd;
	
	String anyStr = new String();
	
	public void setUnamePwd(String uname, String pwd){
		try {
			synchronized (anyStr) {
				System.out.println("线程名为: " + Thread.currentThread().getName()
						+ "在" + System.currentTimeMillis() + "进入同步块");
				this.uname = uname;
				Thread.sleep(3000);
				this.pwd = pwd;
				System.out.println("线程名为: " + Thread.currentThread().getName()
						+ "在" + System.currentTimeMillis() + "离开同步块");
			}
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
	}
}
