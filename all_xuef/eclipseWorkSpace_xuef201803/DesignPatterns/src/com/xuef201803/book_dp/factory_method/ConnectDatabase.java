package com.xuef201803.book_dp.factory_method;

/**
 * 连接数据库
 * @author moveb
 *
 */
public abstract class ConnectDatabase {
	/**
	 * 实际上这里为获取数据库连接，规范了操作流程即模板
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
	 * 返回一个具体实现，由子类完成。
	 * @return
	 */
	protected abstract DriveManager_ factoryMathod();
}
