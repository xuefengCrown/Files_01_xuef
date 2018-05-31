package com.xuef201803.book_dp.factory_method;

/**
 * �������ݿ�
 * @author moveb
 *
 */
public abstract class ConnectDatabase {
	/**
	 * ʵ��������Ϊ��ȡ���ݿ����ӣ��淶�˲������̼�ģ��
	 * @param url
	 * @param user
	 * @param passwd
	 * @return
	 */
	public String getConn(String url, String user, String passwd){
		DriveManager_ driver = factoryMathod();
		String conn = driver.getConnection(url, user, passwd);
		return conn;
	}
	/**
	 * ����һ������ʵ�֣���������ɡ�
	 * @return
	 */
	protected abstract DriveManager_ factoryMathod();
}