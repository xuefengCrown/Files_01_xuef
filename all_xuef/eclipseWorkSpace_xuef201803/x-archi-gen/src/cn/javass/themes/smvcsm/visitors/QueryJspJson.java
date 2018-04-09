package cn.javass.themes.smvcsm.visitors;

import cn.javass.xgen.genconf.vo.ExtendConfModel;
import cn.javass.xgen.genconf.vo.ModuleConfModel;
import cn.javass.xgen.template.visitors.TemplateElement;
import cn.javass.xgen.template.visitors.Visitor;
import java.util.Map;

public class QueryJspJson implements Visitor {

	public Object visitTemplateElement(TemplateElement element) {
		ModuleConfModel moduleConf = element.getModuleConf();
		String voFields[] = ((ExtendConfModel) moduleConf.getMapExtends().get(
				"voFields")).getValues();
		StringBuffer buffer = new StringBuffer("var json ='{");

		for (int i = 0; i < voFields.length; i++){
			if(i==0){
				buffer.append("\""+voFields[i]+"\":\"'+$(\"#"+voFields[i]+"\").val()+'\"");
			}else{
				buffer.append(",\""+voFields[i]+"\":\"'+$(\"#"+voFields[i]+"\").val()+'\"");
			}
		}
		buffer.append("}';");
		return buffer.toString();
	}
}
