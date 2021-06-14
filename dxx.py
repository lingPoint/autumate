#!/usr/bin/env python
# coding=utf-8
import re
import requests
import json
import sys

def main():
    url = "http://dxx.scyol.com/api/student/commit"
    agent = {
        "User-Agent": "抓包获取", #安全第一，用自己的请求头
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


main()



