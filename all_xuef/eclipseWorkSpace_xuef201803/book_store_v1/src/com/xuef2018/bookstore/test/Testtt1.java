package com.xuef2018.bookstore.test;

import java.sql.Connection;

import com.xuef2018.bookstore.db.JDBCUtils;

public class Testtt1 {
	public static void main(String[] args) {
		Connection connection = JDBCUtils.getConnection();
		System.out.println(connection);
	}
}
