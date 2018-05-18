/*
* 封装通用操作
* */
var _util={
    /*
    * type: 请求类型(GET, POST)
    * data: 携带的数据
    * success: 成功后的回调函数
    * */
    ajaxRequest: function (url, type, data, success, error) {
        $.ajax({
            url: url,
            type: type || 'POST',
            data: data,
            success: success,
            error: error
        });
    },
    test: function (who) {
        alert("hello," + who);
    }
}