"use strict";
$(function() {
    
	var _pageSize;
	
	function getBlogsByName(pageIndex, pageSize) {
		 var keyword = $("#index-search-keyword").val();
		 $.ajax({
			 url: "/blogs", 
			 contentType : 'application/json',
			 data:{
				 "async":true, 
				 "pageIndex":pageIndex,
				 "pageSize":pageSize,
				 "keyword": keyword
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
	$("#index-search-btn").click(function() {
		getBlogsByName(0, _pageSize);
	});
	
});