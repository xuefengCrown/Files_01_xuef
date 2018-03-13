package com.xuef2018.dao;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import com.xuef2018.bean.Book;

public class BookDaoPrimitiveImpl implements BookDao {
	private String driverClass = "com.mysql.jdbc.Driver";
	private String url = "jdbc:mysql:///books_2018";
	private String user = "root";
	private String pwd = "121314";
	@Override
	public List<Book> getAllBooks(String username) {
		List<Book> books = new ArrayList<>();
		
		Connection conn = null;
		PreparedStatement ps = null;
		ResultSet rs = null;
		
		try {
			Class.forName(driverClass);
			conn = DriverManager.getConnection(url, user, pwd);
			String sql = "SELECT * FROM tb_books WHERE user_name = ?";
			
			ps = conn.prepareStatement(sql);
			ps.setString(1, username);
			
			rs = ps.executeQuery();
			
			while(rs.next()){
				Book b =new Book();
				b.setBook_name(rs.getString("book_name"));
				b.setUser_name(rs.getString("user_name"));
				b.setBook_id(rs.getInt("id"));
				b.setBook_path(rs.getString("book_path"));
				b.setStars(rs.getInt("stars"));
				b.setLast_modified_time(rs.getString("last_modified_time"));
				System.out.println(b);
				books.add(b);
			}
		} catch (SQLException | ClassNotFoundException e) {
			e.printStackTrace();
		}finally{
			try {
				if(rs != null)
					rs.close();
				if(ps != null)
					ps.close();
				if(conn != null)
					conn.close();
			} catch (SQLException e) {
				e.printStackTrace();
			}
		}
		
		return books;
	}

}
