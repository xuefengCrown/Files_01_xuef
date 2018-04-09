package cn.javass.themes.smvcsm.visitors;

import cn.javass.xgen.genconf.vo.ExtendConfModel;
import cn.javass.xgen.genconf.vo.ModuleConfModel;
import cn.javass.xgen.template.visitors.TemplateElement;
import cn.javass.xgen.template.visitors.Visitor;
import java.util.Map;

public class VoProperty implements Visitor {

	public Object visitTemplateElement(TemplateElement element) {
		ModuleConfModel moduleConf = element.getModuleConf();
		String voFields[] = ((ExtendConfModel) moduleConf.getMapExtends().get(
				"voFields")).getValues();
		
		String voFieldsTypes[] = ((ExtendConfModel) moduleConf.getMapExtends()
				.get("voFieldsTypes")).getValues();
		
		StringBuffer buffer = new StringBuffer("");
		for (int i = 0; i < voFields.length; i++)
			buffer.append((new StringBuilder("private "))
					.append(voFieldsTypes[i]).append(" ").append(voFields[i])
					.append(";\n\t").toString());

		return buffer.toString();
	}
}
