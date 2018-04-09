package cn.javass.themes.smvcsm.visitors;

import cn.javass.xgen.genconf.vo.ExtendConfModel;
import cn.javass.xgen.genconf.vo.ModuleConfModel;
import cn.javass.xgen.template.visitors.TemplateElement;
import cn.javass.xgen.template.visitors.Visitor;

public class InsertIntoValues implements Visitor {

	public Object visitTemplateElement(TemplateElement element) {
		ModuleConfModel moduleConf = element.getModuleConf();
		String voFields[] = ((ExtendConfModel) moduleConf.getMapExtends().get(
				"voFields")).getValues();

		StringBuffer buffer = new StringBuffer("");
		for (int i = 0; i < voFields.length; i++) {
			buffer.append("#{"+voFields[i]+"}");
			if(i<voFields.length-1){
				buffer.append(",");
			}
		}
		return buffer.toString();
	}
}
