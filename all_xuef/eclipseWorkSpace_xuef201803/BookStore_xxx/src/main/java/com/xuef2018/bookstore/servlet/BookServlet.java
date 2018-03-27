package com.xuef2018.bookstore.servlet;

import java.io.IOException;
import java.lang.reflect.Method;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.xuef2018.bookstore.domain.Book;
import com.xuef2018.bookstore.service.BookService;

/**
 * Servlet implementation class BookServlet
 */
public class BookServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
	private BookService bookService = new BookService();

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// 根据 method 参数，调用相应的方法
		String methodName = request.getParameter("method");
		
		try {
			Method method = getClass().getDeclaredMethod(methodName, HttpServletRequest.class, HttpServletResponse.class);
			method.setAccessible(true);
			method.invoke(this, request, response);
		} catch (Exception e) {
			e.printStackTrace();
			throw new RuntimeException(e);
		}		
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doGet(request, response);
	}
	
	/**
	 * 查看所有图书
	 */
	protected void getBooks(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		//System.out.println("getBooks");
		String minPriceStr = req.getParameter("minPrice");
		String maxPriceStr = req.getParameter("maxPrice");
		String pageNoStr = req.getParameter("pageNo");
		int pageNo = 1;
		float minPrice = 0, maxPrice = Integer.MAX_VALUE;
		if(minPriceStr != null && !minPriceStr.equals(""))
			minPrice = Float.parseFloat(minPriceStr);
		if(maxPriceStr != null && !maxPriceStr.equals(""))
			maxPrice = Float.parseFloat(maxPriceStr);
		if(pageNoStr != null)
			pageNo = Integer.parseInt(pageNoStr);
		System.out.println("000000");
		//System.out.println(minPrice + " " + maxPrice + " " + pageNo);
		CriteriaBook criteriaBook = new CriteriaBook(minPrice, maxPrice, pageNo);
		Page<Book> page = bookService.getPage(criteriaBook);
		System.out.println("111111");
		req.setAttribute("allBooks", page);
		System.out.println("222222");
		req.getRequestDispatcher("/WEB-INF/pages/allBooks.jsp").forward(req, resp);
	}
	@Override
	protected void doPut(HttpServletRequest req, HttpServletResponse resp)
			throws ServletException, IOException {
		super.doPut(req, resp);
	}
	@Override
	protected void doDelete(HttpServletRequest req, HttpServletResponse resp)
			throws ServletException, IOException {
		super.doDelete(req, resp);
	}
}
