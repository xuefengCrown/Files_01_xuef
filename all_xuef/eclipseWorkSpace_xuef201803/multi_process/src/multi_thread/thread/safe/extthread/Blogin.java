package multi_thread.thread.safe.extthread;

import multi_thread.thread.safe.LoginServlet;

public class Blogin extends Thread {
	@Override
	public void run() {
		super.run();
		LoginServlet.doPost("b", "bb");
	}
}
