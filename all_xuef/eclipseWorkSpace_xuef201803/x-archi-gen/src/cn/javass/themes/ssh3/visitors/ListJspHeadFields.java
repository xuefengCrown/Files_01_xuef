


// Source File Name:   ListJspHeadFields.java

package cn.javass.themes.ssh3.visitors;

import cn.javass.xgen.genconf.vo.ExtendConfModel;
import cn.javass.xgen.genconf.vo.ModuleConfModel;
import cn.javass.xgen.template.visitors.TemplateElement;
import cn.javass.xgen.template.visitors.Visitor;
import java.util.Map;

public class ListJspHeadFields
    implements Visitor
{

    public ListJspHeadFields()
    {
    }

    public Object visitTemplateElement(TemplateElement element)
    {
        ModuleConfModel moduleConf = element.getModuleConf();
        String voFieldsNames[] = ((ExtendConfModel)moduleConf.getMapExtends().get("colunName_CN")).getValues();
        StringBuffer buffer = new StringBuffer("");
        for(int i = 0; i < voFieldsNames.length; i++)
            buffer.append((new StringBuilder("<td>")).append(voFieldsNames[i]).append("</td>\n\t").toString());

        return buffer.toString();
    }
}
