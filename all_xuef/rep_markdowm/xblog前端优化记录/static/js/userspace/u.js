/*!
 */
$(function() {
	 
	var _pageSize;

	// 根据用户名、页面索引、页面大小获取博客列表
	function getBlogsByName(pageIndex, pageSize) {
		 $.ajax({ 
			 url: "/space/"+  username  +"/blogs",
			 contentType : 'application/json',
			 data:{
				 "async":true, 
				 "pageIndex":pageIndex,
				 "pageSize":pageSize,
				 "catalog":catalogId,
				 "keyword":$("#keyword").val()
			 },
			 success: function(data){
				 $("#mainContainer").html(data);
		     },
		     error : function() {
		    	 toastr.error("error!");
		     }
		 });
	}
	
	// 分页
	$.tbpage("#mainContainer", function (pageIndex, pageSize) {
		getBlogsByName(pageIndex, pageSize);
		_pageSize = pageSize;
	});
   
	// 关键字搜索
	$("#search4an-user").click(function() {
		//getBlogsByName(0, _pageSize);
		var pageIndex = 0;
		var pageSize = 10;
		var searchKeyword = $("#search-keyword").val();
		$.ajax({
			 url: "/space/"+  username  +"/search",
			 contentType : 'application/json',
			 data:{
				 "pageIndex": pageIndex,
				 "pageSize": pageSize,
				 "keyword": searchKeyword
			 },
			 success: function(data){
				 $("#mainContainer").html(data);
		     },
		     error : function() {
		    	 toastr.error("error!");
		     }
		 });
	});
	
	// 获取分类列表
	function getCatalogs(username) {
		// 获取 CSRF Token
		$.ajax({ 
			 url: '/catalogs', 
			 type: 'GET', 
			 data:{"username": username},
			 success: function(data){
				$("#catalogMain").html(data);
		     },
		     error : function() {
		    	 toastr.error("error!");
		     }
		 });
	}
	
	
	// 获取新增分类的页面
	$(".blog-content-container").on("click",".blog-add-catalog", function () {
		$.ajax({
			 url: '/catalogs/edit', 
			 type: 'GET', 
			 success: function(data){
				 $("#catalogFormContainer").html(data);
		     },
		     error : function() {
		    	 toastr.error("error!");
		     }
		 });
	});
	
	// 获取修改某个分类的页面
	$(".blog-content-container").on("click",".blog-edit-catalog", function () { 
		$.ajax({
			 url: '/catalogs/edit/'+$(this).attr('catalogid'),
			 type: 'GET', 
			 success: function(data){
				 $("#catalogFormContainer").html(data);
		     },
		     error : function() {
		    	 toastr.error("error!");
		     }
		 });
	});
	
	// 分类修改后提交
	$("#submitEditCatalog").click(function() {
		// 获取 CSRF Token 
		//var csrfToken = $("meta[name='_csrf']").attr("content");
		//var csrfHeader = $("meta[name='_csrf_header']").attr("content");
 		
		$.ajax({ 
			 url: '/catalogs', 
			 type: 'POST', 
			 contentType: "application/json; charset=utf-8",
			 data: JSON.stringify({
				 "username":username,
				 "catalog":{
					 "id":$('#catalogId').val(),
					 "name":$('#catalogName').val()}}),
			 beforeSend: function(request) {
                 //request.setRequestHeader(csrfHeader, csrfToken); // 添加  CSRF Token
             },
			 success: function(data){
				 if (data.success) {
					 toastr.info(data.message);
					 // 成功后，刷新列表
					 getCatalogs(username);
				 } else {
					 toastr.error(data.message);
				 }
		     },
		     error : function() {
		    	 toastr.error("error!");
		     }
		 });
	});
	
	// 删除分类
	$(".blog-content-container").on("click",".blog-delete-catalog", function () { 
		// 获取 CSRF Token 
		var csrfToken = $("meta[name='_csrf']").attr("content");
		var csrfHeader = $("meta[name='_csrf_header']").attr("content");
 		
		$.ajax({ 
			 url: '/catalogs/'+$(this).attr('catalogid')+'?username='+username, 
			 type: 'DELETE', 
			 beforeSend: function(request) {
                 request.setRequestHeader(csrfHeader, csrfToken); // 添加  CSRF Token 
             },
			 success: function(data){
				 if (data.success) {
					 toastr.info(data.message);
					 // 成功后，刷新列表
					 getCatalogs(username);
				 } else {
					 toastr.error(data.message);
				 }
		     },
		     error : function() {
		    	 toastr.error("error!");
		     }
		 });
	});
	
	// 根据分类查询
	$(".blog-content-container").on("click",".blog-query-by-catalog", function () { 
		catalogId = $(this).attr('catalogId');
		getBlogsByName(0, _pageSize);
	});

	getCatalogs(username);
});