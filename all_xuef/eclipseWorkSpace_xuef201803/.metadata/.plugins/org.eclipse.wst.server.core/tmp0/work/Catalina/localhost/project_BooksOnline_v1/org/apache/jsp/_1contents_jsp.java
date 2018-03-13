package org.apache.jsp;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.jsp.*;

public final class _1contents_jsp extends org.apache.jasper.runtime.HttpJspBase
    implements org.apache.jasper.runtime.JspSourceDependent {

  private static final javax.servlet.jsp.JspFactory _jspxFactory =
          javax.servlet.jsp.JspFactory.getDefaultFactory();

  private static java.util.List<java.lang.String> _jspx_dependants;

  private javax.el.ExpressionFactory _el_expressionfactory;
  private org.apache.tomcat.InstanceManager _jsp_instancemanager;

  public java.util.List<java.lang.String> getDependants() {
    return _jspx_dependants;
  }

  public void _jspInit() {
    _el_expressionfactory = _jspxFactory.getJspApplicationContext(getServletConfig().getServletContext()).getExpressionFactory();
    _jsp_instancemanager = org.apache.jasper.runtime.InstanceManagerFactory.getInstanceManager(getServletConfig());
  }

  public void _jspDestroy() {
  }

  public void _jspService(final javax.servlet.http.HttpServletRequest request, final javax.servlet.http.HttpServletResponse response)
        throws java.io.IOException, javax.servlet.ServletException {

    final javax.servlet.jsp.PageContext pageContext;
    javax.servlet.http.HttpSession session = null;
    final javax.servlet.ServletContext application;
    final javax.servlet.ServletConfig config;
    javax.servlet.jsp.JspWriter out = null;
    final java.lang.Object page = this;
    javax.servlet.jsp.JspWriter _jspx_out = null;
    javax.servlet.jsp.PageContext _jspx_page_context = null;


    try {
      response.setContentType("text/html; charset=UTF-8");
      pageContext = _jspxFactory.getPageContext(this, request, response,
      			null, true, 8192, true);
      _jspx_page_context = pageContext;
      application = pageContext.getServletContext();
      config = pageContext.getServletConfig();
      session = pageContext.getSession();
      out = pageContext.getOut();
      _jspx_out = out;

      out.write("\r\n");
      out.write("<!DOCTYPE html PUBLIC \"-//W3C//DTD HTML 4.01 Transitional//EN\" \"http://www.w3.org/TR/html4/loose.dtd\">\r\n");
      out.write("<html>\r\n");
      out.write("<head>\r\n");
      out.write("<meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\">\r\n");
      out.write("<title>Insert title here</title>\r\n");
      out.write("\r\n");
      out.write("<link rel=\"stylesheet\" type=\"text/css\" href=\"simditor/styles/simditor.css\" />\r\n");
      out.write("\r\n");
      out.write("<script type=\"text/javascript\" src=\"simditor/scripts/jquery.min.js\"></script>  \r\n");
      out.write("<script type=\"text/javascript\" src=\"simditor/scripts/module.js\"></script>  \r\n");
      out.write("<script type=\"text/javascript\" src=\"simditor/scripts/hotkeys.js\"></script>\r\n");
      out.write("<script type=\"text/javascript\" src=\"simditor/scripts/uploader.js\"></script>  \r\n");
      out.write("<script type=\"text/javascript\" src=\"simditor/scripts/simditor.js\"></script> \r\n");
      out.write("\r\n");
      out.write("<script type=\"text/javascript\">\r\n");
      out.write("\t\r\n");
      out.write("\t$(function(){\r\n");
      out.write("\t\tSimditor.locale = 'zh-CN';//设置中文\r\n");
      out.write("        var editor = new Simditor({\r\n");
      out.write("            textarea: $('#editor'),  //textarea的id\r\n");
      out.write("            placeholder: '这里输入文字...',\r\n");
      out.write("            toolbar:  ['title', 'bold', 'italic', 'underline', 'strikethrough', 'fontScale', 'color', '|', 'ol', 'ul', 'blockquote', 'code', 'table', '|', 'link', 'image', 'hr', '|', 'indent', 'outdent', 'alignment'], //工具条都包含哪些内容\r\n");
      out.write("            pasteImage: true,//允许粘贴图片\r\n");
      out.write("            defaultImage: '/res/simditor/images/image.png',//编辑器插入的默认图片，此处可以删除\r\n");
      out.write("            upload : {\r\n");
      out.write("                url : 'richtext_img_upload.do', //文件上传的接口地址\r\n");
      out.write("                params: null, //键值对,指定文件上传接口的额外参数,上传的时候随文件一起提交\r\n");
      out.write("                fileKey: 'upload_file', //服务器端获取文件数据的参数名\r\n");
      out.write("                connectionCount: 3,\r\n");
      out.write("                leaveConfirm: '正在上传文件'\r\n");
      out.write("            }\r\n");
      out.write("        });\r\n");
      out.write("        // call setValue to set content\r\n");
      out.write("        editor.setValue('#hello world')\r\n");
      out.write("\t});\r\n");
      out.write("</script>\r\n");
      out.write("\r\n");
      out.write("</head>\r\n");
      out.write("<body>\r\n");
      out.write("\r\n");
      out.write("\t<textarea id=\"editor\" placeholder=\"Balabala\" autofocus></textarea>\r\n");
      out.write("</body>\r\n");
      out.write("</html>");
    } catch (java.lang.Throwable t) {
      if (!(t instanceof javax.servlet.jsp.SkipPageException)){
        out = _jspx_out;
        if (out != null && out.getBufferSize() != 0)
          try { out.clearBuffer(); } catch (java.io.IOException e) {}
        if (_jspx_page_context != null) _jspx_page_context.handlePageException(t);
      }
    } finally {
      _jspxFactory.releasePageContext(_jspx_page_context);
    }
  }
}
