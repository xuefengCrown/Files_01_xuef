<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@taglib prefix='c' uri="http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>员工列表</title>
</head>
<body>
	<table>
			<tr>
				<td>e_no</td>
				<td>e_name</td>
			</tr>
		<c:forEach items="${allemp}"  var="emp" >
			<tr>
				<td>${emp.e_no }</td>
				<td>${emp.e_name }</td>
			</tr>
		</c:forEach>
	</table>
</body>
</html>