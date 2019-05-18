import http.client
import hashlib
import json
import urllib
import random

def baidu_translate(content,fromlang,tolang):
    appid = '20190518000298824'
    secretKey = 'KRlIbCBScKSyzu15RZe0'
    httpClient = None
    myurl = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
    q = content
    fl = fromlang # 源语言
    tl = tolang   # 翻译后的语言
    salt = random.randint(32768, 65536)   #产生一个范围内的整形随机数
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(
        q) + '&from=' + fl + '&to=' + tl + '&salt=' + str(
        salt) + '&sign=' + sign

    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
        # response是HTTPResponse对象
        response = httpClient.getresponse()
        jsonResponse = response.read().decode("utf-8")# 获得返回的结果，结果为json格式
        js = json.loads(jsonResponse)  # 将json格式的结果转换字典结构
        dst = str(js["trans_result"][0]["dst"])  # 取得翻译后的文本结果
        return dst # 打印结果
    except Exception as e:
        return e
    finally:
        if httpClient:
            httpClient.close()

if __name__ == '__main__':
       baidu_translate(content)

