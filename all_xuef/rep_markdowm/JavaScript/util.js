
/* xuef 的工具包*/

var util = {
	// 将json格式的字符串转换为json对象
	jsonParse: function(str){
		/*
		var jsonObj = null;
		try{
			jsonObj = JSON.parse(str);
		}
		catch(e){
			// IE6,7下,没有JSON.parse
			jsonObj = eval("(" + str + ")");
		}
		*/
		return "JSON" in window? JSON.parse(str) : eval("(" + str + ")");
	}
};