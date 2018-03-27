<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" 
			"http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>'()</title>
<%
	pageContext.setAttribute("emp_path", request.getContextPath());
%>

<!-- jQuery -->
<script src="${emp_path}/js/jquery-1.10.1.js"></script>
<!-- Bootstrap 核心 CSS 文件 -->
<link rel="stylesheet"
	href="${emp_path}/css/bootstrap-3.3.7-dist/css/bootstrap.min.css" />
<!-- Bootstrap 核心 JavaScript 文件 -->
<script src="${emp_path}/css/bootstrap-3.3.7-dist/js/bootstrap.min.js"></script>

</head>
<body>
	<div class="container">
		<!-- 标题 -->
		<div class="row">
		  	<div class="col-md-12"><h1>EmpsAdmS</h1></div>
		</div>
		
		<!-- 标题一般操作 -->
		<div class="row">
		  	<div class="col-md-4 col-md-offset-9">
		  		<button type="button" class="btn btn-primary"> 
		  			 Add <span class="glyphicon glyphicon-plus"></span></button>
		  		<button type="button" class="btn btn-danger"> 
		  			 DelALL<span class="glyphicon glyphicon-remove"></span></button>
			</div>
		</div>
		<div class="row">
		  	<div class="col-md-12"><h4>******</h4></div>
		</div>
		<!-- 数据展示 -->
		<div class="row">
			<div class="col-md-12">
				<table class="table table-bordered table-hover" id="emps_table">
					<thead>
						<tr class="info">
							<th>工号</th>
							<th>姓名</th>
							<th>性别</th>
							<th>岗位</th>
							<th>部门</th>
							<th>地点</th>
							<th>操作</th>
						</tr>
					</thead>
					<tbody>
					
					</tbody>
				</table>
			</div>
		</div>
		
		<!-- 分页信息 -->
		<div class="row">
			<div class="col-md-6" id="page_info">
				
			</div>
			<div class="col-md-6" id="page_nav">
			</div>
		</div>
	</div>
	<!-- 页面加载完成后执行 -->
	<script type="text/javascript">
		$(function(){
			to_page(1)
		})
		function to_page(pageNo){
			$.ajax({
				url: "${emp_path}/emps",
				type: "get",
				data: "pageNo="+pageNo,
				success: function(emps){
					console.log(emps)
					getDepts(emps);
				}
			})
		}
		// 查询所有部门信息
		function getDepts(emps){
			$.ajax({
				url: "${emp_path}/depts",
				type: "get",
				success: function(depts){
					console.log(depts)
					build_emps(emps, depts)
					build_page_info(emps, depts)
					build_page_nav(emps, depts)
				}
			});
		}
		// 构建员工列表
		function build_emps(res, depts){
			$("#emps_table tbody").empty()
			var emps = res.res.pageInfo.list
			$.each(emps, function(index, item){
				var eNoInput = $("<input></input>")
											.attr("type", "text")
											.attr("readonly", "true")
											.addClass("form-control")
											.attr("size", "1")
											.attr("name", "eNo")
				var eNameInput = $("<input/>").attr("type", "text")
											  .attr("readonly", "true")
											  .addClass("form-control")
											  .attr("size", "3")
											  .attr("name", "eName")
											  
				var eGenderInput = $("<select></select>").addClass("form-control")
													.attr("readonly", "true")
													.attr("size", "1")
													.attr("name", "eGender")
													.append("<option value='m'>男</option>")
													.append("<option value='f'>女</option>")
				
				var eJobInput = $("<input />").attr("type", "text")
											  .attr("readonly", "true")
											  .attr("name", "eJob")
											.addClass("form-control")
											.attr("size", "5")
											
				var dNameInput = $("<select></select>").addClass("form-control")
													.attr("readonly", "true")
													.attr("size", "1")
													.attr("name", "dNo")
				
				$.each(depts.res.depts, function(index, item){
					//console.log(item.dNo)
					dNameInput.append("<option value='"+ item.dNo + "'>" + item.dName +"</option>")
				});
				
				var dLocInput = $("<input />").attr("type", "text")
												.attr("readonly", "true")
												.attr("name", "dLocation")
											.addClass("form-control")
											.attr("size", "4")
				
				var eNoTd = $("<td></td>").append(eNoInput.val(item.eNo))
				var eNameTd = $("<td></td>").append(eNameInput.val(item.eName))
				var eGenderTd = $("<td></td>").append(eGenderInput.val(item.eGender))
				var eJobTd = $("<td></td>").append(eJobInput.val(item.eJob))
				var deptNameTd = $("<td></td>").append(dNameInput.val(item.department.dNo))
				var deptLocTd = $("<td></td>").append(dLocInput.val(item.department.dLocation))
				var inp = $(this).parent().siblings()
				var isEditable = inp.children().last().attr("readonly")==true
				
				var saveClickBind = false;
				var btn = $("<button></button>")
								.attr("type","button")
								.addClass("btn btn-primary btn-sm")
								.text("Edit")
								.click(function(){
									// 点击edit button时，将对应input设置为可编辑状态
									//alert("isEditable " + isEditable)
									// edit 按钮 转为 save 按钮
									if(!isEditable){
										//alert("click edit")
										$(this).empty()
										var records = $(this).parent().siblings().children();
										$(this).addClass("btn-warning")
											.append("Sav<span class='glyphicon glyphicon-save'></span>")
										
										// 为save绑定事件; 这儿的逻辑有点乱
										if(!saveClickBind
												&& $(this).hasClass("btn-warning")){
											//alert("为save绑定事件");
											$(this).click(function(){
												// 是save操作时才执行
												var newEmp = {};
												if(!$(this).hasClass("btn-warning")){
													$.each(records, function(idx, item){
														alert($(item).attr("name") + " : " + $(item).val());
														
													})
													alert("save emp");
												}
											});
											saveClickBind = true;
										};
											
										records.removeAttr("readonly")
										records.first().attr("readonly", true)
										
										isEditable = true
									}else{
										//alert("click save")
										$(this).empty()
										$(this).removeClass("btn-warning")
											.addClass("btn-primary")
											.append("Edit<span class='glyphicon glyphicon-pencil'></span>")
										$(this).parent().siblings().children().attr("readonly", true)
										
										isEditable = false
									}
								})
								.append($("<span></span>")
								.addClass("glyphicon glyphicon-pencil"));
				
				var opeTd = $("<td></td>")
						.append(btn)
						.append(" ")
						.append($("<button></button>")
									.attr("type","button")
									.addClass("btn btn-danger btn-sm")
									.text("DeL")
									.append($("<span></span>")
									.addClass("glyphicon glyphicon-remove")))
				$("<tr></tr>").append(eNoTd).append(eNameTd).append(eGenderTd)
							  .append(eJobTd).append(deptNameTd).append(deptLocTd)
							  .append(opeTd)
							  .appendTo("#emps_table tbody")
			})
		}
		// 分页信息
		function build_page_info(res){
			$("#page_info").empty()
			var page_info_json = res.res.pageInfo
			$("#page_info").append("当前第 "+ page_info_json.pageNum + 
					" 页 共 " + page_info_json.pages + " 页 " + page_info_json.total + " 条记录")
		}
		// 分页导航
		function build_page_nav(res){
			$("#page_nav").empty()
			var page_info_json = res.res.pageInfo
			var nav = $("<nav></nav>")
			var par_ul = $("<ul></ul>").addClass("pagination")
			var first = $("<li></li>").append($("<a></a>").append("首页"));
			
			var pre = $("<li></li>").append($("<a></a>")
											.append("&laquo;"));
			
			// 没有前一页时，禁用首页和pre链接
			if(page_info_json.hasPreviousPage == false){
				first.addClass("disabled")
				pre.addClass("disabled")
			}else{
				first.click(function(){
					to_page(1);
				});
				pre.click(function(){
					to_page(page_info_json.pageNum-1)
				});
			}
			var next = $("<li></li>").append($("<a></a>").append("&raquo;"));
			var last = $("<li></li>").append($("<a></a>").append("末页"));
			// 没有后一页时，禁用末页和next链接
			if(page_info_json.hasNextPage == false){
				next.addClass("disabled")
				last.addClass("disabled")
			}else{
				next.click(function(){
					to_page(page_info_json.pageNum+1)
				});
				
				last.click(function(){
					to_page(page_info_json.pages)
				});
			}
				
			par_ul.append(first).append(pre)
			
			$.each(page_info_json.navigatepageNums, function(index, item){
				var cur = $("<li></li>").append($("<a></a>").append(item)
													.click(function(){
														to_page(item)
													}));
				// 高亮当前页
				if(page_info_json.pageNum == item){
					cur.addClass("active");
				}
				par_ul.append(cur)
				par_ul.append(next).append(last)
			})
			nav.append(par_ul)
			$("#page_nav").append(nav)
		}
	</script>
</body>
</html>