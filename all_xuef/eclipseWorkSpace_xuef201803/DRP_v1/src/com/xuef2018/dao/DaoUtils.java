package com.xuef2018.dao;

import java.io.IOException;
import java.io.InputStream;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.Properties;

/*
 * �������ݿ� ������
 */
public class DaoUtils {
	public Connection getConnection(){
		String driverClass = null;
		String url = null;
		String user = null;
		String pwd = null;
		
		Connection connection = null;
		// ���� ���ݿ����ӵ� �����ļ�
		InputStream resourceAsStream = 
				getClass().getClassLoader().getResourceAsStream("db.properties");
		Properties properties = new Properties();
		try {
			properties.load(resourceAsStream);
			// ��ȡ�����ļ�
			driverClass = properties.getProperty("mysql.driverClass");
			url = properties.getProperty("mysql.url");
			user = properties.getProperty("mysql.user");
			pwd = properties.getProperty("mysql.password");
			
			//2. �������ݿ���������(��Ӧ�� Driver ʵ��������ע�������ľ�̬�����.)
			Class.forName(driverClass);
			
			//3. ͨ�� DriverManager �� getConnection() ������ȡ���ݿ�����. 
			connection = 
					DriverManager.getConnection(url, user, pwd);
			System.out.println(connection); 
		} catch (IOException | SQLException | ClassNotFoundException e) {
			e.printStackTrace();
		}
		
		return connection;
	}
}