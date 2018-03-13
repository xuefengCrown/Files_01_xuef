package com.xuef2018.servlet;

import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class OpenBookServlet extends HttpServlet {
	@Override
	protected void doGet(HttpServletRequest req, HttpServletResponse resp)
			throws ServletException, IOException {
		String book_id = req.getParameter("id");
		System.out.println(book_id);
		String path = book_id + "contents.jsp";
		req.getRequestDispatcher("/" + path).forward(req, resp);
	}
}
