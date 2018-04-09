package cn.javass.themes.smvcsm.visitors;

import cn.javass.xgen.genconf.vo.ExtendConfModel;
import cn.javass.xgen.genconf.vo.ModuleConfModel;
import cn.javass.xgen.template.visitors.TemplateElement;
import cn.javass.xgen.template.visitors.Visitor;
import java.util.Map;

public class QueryJspFields implements Visitor {

	public Object visitTemplateElement(TemplateElement element) {
		ModuleConfModel moduleConf = element.getModuleConf();
		String voFields[] = ((ExtendConfModel) moduleConf.getMapExtends().get(
				"voFields")).getValues();
		String voFieldsTypes[] = ((ExtendConfModel) moduleConf.getMapExtends()
				.get("voFieldsTypes")).getValues();
		String voFieldsNames[] = ((ExtendConfModel) moduleConf.getMapExtends()
				.get("voFieldsNames")).getValues();
		StringBuffer buffer = new StringBuffer("");
		int count = 0;
		for (int i = 0; i < voFields.length; i++) {
			if (count == 0){
				buffer.append("<tr>\n\t");
			}
			buffer.append((new StringBuilder("<td>")).append(voFieldsNames[i])
					.append("</td>\n\t").toString());
			buffer.append((new StringBuilder("<td><input type=\"text\" id=\""
					+ voFields[i].trim() + "\" name=\"")).append(voFields[i].trim())
					.append("\" ></td>\n\t").toString());
			if (++count == 2) {
				buffer.append("</tr>\n");
				count = 0;
			}
		}

		// count = 0;
		// String qmVoFields[] = ((ExtendConfModel) moduleConf.getMapExtends()
		// .get("qmVoFields")).getValues();
		// String qmVoFieldsNames[] = ((ExtendConfModel) moduleConf
		// .getMapExtends().get("qmVoFieldsNames")).getValues();
		// for (int i = 0; i < voFields.length; i++)
		// if (isNumber(voFieldsTypes[i])) {
		// buffer.append("<tr>\n\t");
		// int qmIndex = qmHasField(
		// (new StringBuilder(String.valueOf(voFields[i])))
		// .append("2").toString(), qmVoFields);
		// if (qmIndex > 0) {
		// buffer.append((new StringBuilder("<td>"))
		// .append(voFieldsNames[i])
		// .append("\u5927\u4E8E\u7B49\u4E8E</td>\n\t")
		// .toString());
		// buffer.append((new StringBuilder(
		// "<td><input type=\"text\" name=\"qm."))
		// .append(voFields[i]).append("\" ></td>\n\t")
		// .toString());
		// buffer.append((new StringBuilder("<td>"))
		// .append(qmVoFieldsNames[qmIndex - 1])
		// .append("</td>\n\t").toString());
		// buffer.append((new StringBuilder(
		// "<td><input type=\"text\" name=\"qm."))
		// .append(qmVoFields[qmIndex - 1])
		// .append("\"></td>\n").toString());
		// } else {
		// buffer.append((new StringBuilder("<td>"))
		// .append(voFieldsNames[i]).append("</td>\n\t")
		// .toString());
		// buffer.append((new StringBuilder(
		// "<td><input type=\"text\" name=\"qm."))
		// .append(voFields[i]).append("\" ></td>\n\t")
		// .toString());
		// }
		// buffer.append("</tr>\n");
		// }

		return buffer.toString();
	}

	private int qmHasField(String fName, String qmVoFields[]) {
		for (int i = 1; i <= qmVoFields.length; i++)
			if (qmVoFields[i - 1].equals(fName))
				return i;

		return 0;
	}

	private boolean isNumber(String type) {
		return "int".equals(type) || "Integer".equals(type)
				|| "float".equals(type) || "Float".equals(type)
				|| "double".equals(type) || "Double".equals(type);
	}
}
