


// Source File Name:   EditFormInputs.java

package cn.javass.themes.smvcsh.visitors;

import cn.javass.xgen.genconf.vo.ExtendConfModel;
import cn.javass.xgen.genconf.vo.ModuleConfModel;
import cn.javass.xgen.template.visitors.TemplateElement;
import cn.javass.xgen.template.visitors.Visitor;
import java.util.Map;

public class EditFormInputs
    implements Visitor
{

    public EditFormInputs()
    {
    }

    public Object visitTemplateElement(TemplateElement element)
    {
        ModuleConfModel moduleConf = element.getModuleConf();
        return genProperties(moduleConf, "voFields", "voFieldsNames", "fieldNeedValidates", "validateMsgs");
    }

    private static String genProperties(ModuleConfModel moduleConf, String fieldsName, String fieldsNames, String fieldNeedValidatesName, String validateMsgsName)
    {
        String voFields[] = ((ExtendConfModel)moduleConf.getMapExtends().get(fieldsName)).getValues();
        String voFieldsNames[] = ((ExtendConfModel)moduleConf.getMapExtends().get(fieldsNames)).getValues();
        String fieldNeedValidates[] = ((ExtendConfModel)moduleConf.getMapExtends().get(fieldNeedValidatesName)).getValues();
        String validateMsgs[] = ((ExtendConfModel)moduleConf.getMapExtends().get(validateMsgsName)).getValues();
        StringBuffer buffer = new StringBuffer("");
        for(int i = 0; i < voFields.length; i++)
        {
            buffer.append("<div class=\"control-group\">\n\t");
            buffer.append((new StringBuilder("<form:label path=\"")).append(voFields[i]).append("\" cssClass=\"control-label\">").append(voFieldsNames[i]).append("</form:label>\n").toString());
            buffer.append("<div class=\"controls\">\n\t");
            buffer.append((new StringBuilder("<form:input path=\"")).append(voFields[i]).append("\"").toString());
            if("true".equals(fieldNeedValidates[i]))
                buffer.append((new StringBuilder(" cssClass=\"validate[required]\" placeholder=\"")).append(validateMsgs[i]).append("\"").toString());
            buffer.append(" />\n");
            buffer.append("</div>\n");
            buffer.append("</div>");
            buffer.append("\n\t");
        }

        return buffer.toString();
    }
}
