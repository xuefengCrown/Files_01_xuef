package multi_thread.thread.safe;

// ģ��һ�� Servlet ���
public class LoginServlet {
	private static String usernameRef;
	private static String passwordRef;
	
	public static void doPost(String username, String password){
		try{
			usernameRef = username;
			if("a".equals(username)){
				Thread.sleep(5000);
			}
			passwordRef = password;
			System.out.println("username = " + usernameRef + 
					" password = " + password);
		} catch(Exception e){
			e.printStackTrace();
		}
	}
}