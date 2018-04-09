


// Source File Name:   ListTableValues.java

package cn.javass.themes.smvcsh.visitors;

import cn.javass.xgen.genconf.vo.ExtendConfModel;
import cn.javass.xgen.genconf.vo.ModuleConfModel;
import cn.javass.xgen.template.visitors.TemplateElement;
import cn.javass.xgen.template.visitors.Visitor;
import java.util.Map;

public class ListTableValues
    implements Visitor
{

    public ListTableValues()
    {
    }

    public Object visitTemplateElement(TemplateElement element)
    {
        ModuleConfModel moduleConf = element.getModuleConf();
        return genProperties(moduleConf, "voFields");
    }

    private static String genProperties(ModuleConfModel moduleConf, String fieldsName)
    {
        String voFields[] = ((ExtendConfModel)moduleConf.getMapExtends().get(fieldsName)).getValues();
        StringBuffer buffer = new StringBuffer("");
        for(int i = 0; i < voFields.length; i++)
        {
            buffer.append((new StringBuilder("<td>${m.")).append(voFields[i]).append("}</td> ").toString());
            buffer.append("\n\t");
        }

        return buffer.toString();
    }
}
