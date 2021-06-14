#!/usr/bin/env python
# coding: utf-8

# # 获取数据 6、10

# In[14]:


# coding=utf-8
import re
import requests
import json
import sys


# In[15]:


def main():
    url = "http://dxx.scyol.com/api/student/commit"
    agent = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; MI 8 SE Build/QKQ1.190828.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045617 Mobile Safari/537.36 MMWEBID/3048 MicroMessenger/8.0.3.1880(0x2800033F) Process/tools WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64",
        'Content-Type': 'application/json',
        "token":"抓包获取", #抓包获取！！！
    }
    #抓包获取数据！！！
    data = {"name":"", #名字
            "tel":"", #电话
            "org":"",
            "lastOrg":12364,
            "orgName":"", #
            "allOrgName":"",
           }
    r = requests.post(url,headers=agent,data=json.dumps(data))
    r.encoding='utf-8'
    print(r.text)


# In[16]:


main()


# In[ ]:

