package com.xuef201803.book_dp.factory_method;

public interface DriveManager_ {
	// 连接数据库 JDBC返回的是Connection
	String getConnection(String url, String user, String passwd);
}
