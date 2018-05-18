package com.xuef201803.book_dp.factory_method;

public class Client {
	public static void main(String[] args) {
		ConnectDatabase connectDb = new ConnectMysqlDB();
		connectDb.getConn("url", "user", "passwd");
	}
}
