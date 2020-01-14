#黄金
import json,urllib
from urllib.parse import urlencode
# 上海黄金交易所
def request1(appkey='7e71ac026772617efa281376815d1696', m="GET"):
    url = "http://web.juhe.cn:8080/finance/gold/shgold"
    params = {
        "key": appkey,  # APP Key
        "v": "",  # JSON格式版本(0或1)默认为0

    }
    params = urlencode(params)
    if m == "GET":
        f = urllib.request.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.request.urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            return res
        else:
            print
            "%s:%s" % (res["error_code"], res["reason"])
    else:
        print
        "request api error"