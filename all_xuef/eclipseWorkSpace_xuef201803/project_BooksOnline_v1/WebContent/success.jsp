<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8" import="java.util.List" import="com.xuef2018.bean.Book" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Insert title here</title>
</head>
<body>
	Welcome
	
	<% 
		List<Book> books = (List<Book>)request.getAttribute("all_books");
		for (Book book: books){
	%>
		<%= book.getBook_name() %><br>
	<% 
		}
	%>
</body>
</html>