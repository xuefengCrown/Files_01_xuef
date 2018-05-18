"use strict";
$(function() {

    // 初始化下拉
    $('.form-control-chosen').chosen();

    // 初始化标签(当编辑某篇博客时，需要初始化博客标签)
	// 后面可以在创建博客中加入自动分析博客内容以提取标签的功能

 	// 发布博客
 	$("#submitBlog").click(function() {
		// 获取 CSRF Token

		$.ajax({
		    url: '/space/'+ $(this).attr("username") + '/blogs/edit',
		    type: 'POST',
			contentType: "application/json; charset=utf-8",
		    data:JSON.stringify({"id":$('#blogId').val(), 
		    	"title": $('#title').val(), 
		    	"summary": $('#summary').val() , 
		    	"content": $('#md-content').val(),
		    	"catalog":{"id":$('#catalogSelect').val()},
		    	"tags":$('#tags_1').val()
		    	}),
			beforeSend: function(request) {
			},
			 success: function(data){
				 if (data.success) {
					 // 成功后，重定向
					 console.log(data);
					 var redirectUrl = data.data;
					 window.location = redirectUrl;
				 } else {
					 toastr.error("error!"+data.message);
				 }
		     },
		     error : function() {
		    	 toastr.error("error!");
		     }
		})
 	})
});