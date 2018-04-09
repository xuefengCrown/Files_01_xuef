package cn.javass.themes.smvcsm.visitors;

import cn.javass.xgen.genconf.vo.ExtendConfModel;
import cn.javass.xgen.genconf.vo.ModuleConfModel;
import cn.javass.xgen.template.visitors.TemplateElement;
import cn.javass.xgen.template.visitors.Visitor;
import java.util.Map;

public class QueryModelToString implements Visitor {
	public Object visitTemplateElement(TemplateElement element) {
		ModuleConfModel moduleConf = element.getModuleConf();
		String voFields[] = ((ExtendConfModel) moduleConf.getMapExtends().get(
				"qmVoFields")).getValues();
		StringBuffer buffer = new StringBuffer(
				"\"Model\"+this.getClass().getName()+\",\"+super.toString()+\" ,[");
		for (int i = 0; i < voFields.length; i++)
			if (voFields[i] != null && voFields[i].trim().length() != 0) {
				String fName = voFields[i];
				buffer.append((new StringBuilder()).append(fName)
						.append("=\" + this.get")
						.append(fName.substring(0, 1).toUpperCase())
						.append(fName.substring(1)).append("() + \",")
						.toString());
			}

		buffer.append("]\"");
		return buffer.toString();
	}
}
