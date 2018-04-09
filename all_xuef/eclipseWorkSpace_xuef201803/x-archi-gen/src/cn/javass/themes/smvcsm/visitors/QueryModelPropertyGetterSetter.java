package cn.javass.themes.smvcsm.visitors;

import cn.javass.xgen.genconf.vo.ExtendConfModel;
import cn.javass.xgen.genconf.vo.ModuleConfModel;
import cn.javass.xgen.template.visitors.TemplateElement;
import cn.javass.xgen.template.visitors.Visitor;
import java.util.Map;

public class QueryModelPropertyGetterSetter implements Visitor {

	public Object visitTemplateElement(TemplateElement element) {
		ModuleConfModel moduleConf = element.getModuleConf();
		String voFields[] = ((ExtendConfModel) moduleConf.getMapExtends().get(
				"qmVoFields")).getValues();
		String voFieldsTypes[] = ((ExtendConfModel) moduleConf.getMapExtends()
				.get("qmVoFieldsTypes")).getValues();
		StringBuffer buffer = new StringBuffer("");
		for (int i = 0; i < voFields.length; i++)
			if (voFields[i] != null && voFields[i].trim().length() != 0) {
				buffer.append((new StringBuilder("public void set"))
						.append(voFields[i].substring(0, 1).toUpperCase())
						.append(voFields[i].substring(1)).append("(")
						.append(voFieldsTypes[i]).append(" obj){\n\t\t")
						.toString());
				buffer.append((new StringBuilder("this.")).append(voFields[i])
						.append(" = obj;\n\t").toString());
				buffer.append("}\n\t");
				buffer.append((new StringBuilder("public "))
						.append(voFieldsTypes[i]).append(" get")
						.append(voFields[i].substring(0, 1).toUpperCase())
						.append(voFields[i].substring(1)).append("(){\n\t\t")
						.toString());
				buffer.append((new StringBuilder("return this."))
						.append(voFields[i]).append(";\n\t").toString());
				buffer.append("}\n\t");
				buffer.append("\n\t");
			}

		return buffer.toString();
	}
}
