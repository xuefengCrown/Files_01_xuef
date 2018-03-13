package com.xuef2018.servlet;

import java.io.IOException;
import java.util.Arrays;
import java.util.List;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.xuef2018.bean.Book;
import com.xuef2018.dao.BookDao;
import com.xuef2018.dao.BookDaoPrimitiveImpl;

/**
 * Servlet implementation class LoginSuccessServlet
 */
public class LoginSuccessServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
       

	protected void doGet(HttpServletRequest request, 
			HttpServletResponse response) 
					throws ServletException, IOException {
		
		// 查询数据库，获取信息
		BookDao bookDao = new BookDaoPrimitiveImpl();
		String username = request.getParameter("username");
		List<Book> allBooks = bookDao.getAllBooks(username );
		System.out.println(allBooks);
		request.setAttribute("all_books", allBooks);
		request.setAttribute("user_name", username);
		request.getRequestDispatcher("/success.jsp").forward(request, response);
	}

	protected void doPost(HttpServletRequest request, 
			HttpServletResponse response) throws ServletException, IOException {
	}

}
