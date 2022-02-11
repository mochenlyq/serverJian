import requests
key = ""
url = "https://sc.ftqq.com/%s.send"%(key)
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'}
payload = {'text': '签到成功', 'desp': 'Python用Server酱推送微信模板消息'}
requests.post(url, params=payload, headers=headers)