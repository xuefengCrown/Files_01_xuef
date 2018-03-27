<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="s" uri="/struts-tags" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>'()-xuef</title>
<script type="text/javascript" src="js/jquery-1.10.1.min.js"></script>
<script type="text/javascript">
	$(function(){
		
		$("input[name='username']").change(function(){
			var $username = $("input[name='username']")
			var username = $username.val()
			var data = {'username': username}
			var url = "book-logincheck.action"
			$("#userName").load(url, data);
		})
		$("input[name='password']").change(function(){
			var $username = $("input[name='username']")
			var username = $username.val()
			var $pwd = $("input[name='password']")
			var pwd = $pwd.val()
			var data = {'username':username,
						'pwd': pwd}
			var url = "book-logincheckpwd.action"
			$("#pwd").load(url, data);
		})
	})
</script>
</head>
<body>
	<br><br>
	<center>
		购物车中有 <span class="emphasis"> ${cart.totalNum}</span> 本书<br>
		一共  <span class="emphasis"> ${cart.totalMoney}</span> 元<br>
		<s:if test="#session.cart == null">
			'()
		</s:if>
		<s:else>
			<table>
				<tr>
					<td>TITLE</td>
					<td>QUA</td>
					<td>OPE</td>
				</tr>
				<s:iterator value="#session.seeCart">
					<tr>
						<td><s:property value="book.title"/></td>
						<td><s:property value="bookNum"/></td>
						<td><a href="book-deleteRecord.action?id=${book.id}">删除</a></td>
					</tr>
				</s:iterator>
			</table>
		</s:else>
		<br><br>
		<form action="book-login2pay.action"
				method="POST">
			<div>
				<input type="text" name="username" /><br>
				<span id="userName"></span>
			</div>
			<div>
				<input type="password" name="password" /><br>
				<span id="pwd"></span>
			</div>
			<input type="submit" value="login2pay" />
		</form>
	</center>
</body>
</html>