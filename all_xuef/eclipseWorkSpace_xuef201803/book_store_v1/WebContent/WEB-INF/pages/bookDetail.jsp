<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Insert title here</title>
</head>
<body>
	书名: ${book.title }<br>
	作者: ${book.author }<br>
	价格: ${book.price }<br>
	出版日期: ${book.publishingdate }<br>
	销量: ${book.salesamount }<br><br>
	<a href="lookoverAllBooksServlet?method=getBooks&pageNo=${param.pageNo}
	&minPrice=${param.minPrice}&maxPrice=${param.maxPrice}">继续购物</a>
</body>
</html>