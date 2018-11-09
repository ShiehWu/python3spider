# -*- coding: utf-8 -*-
"""
    :author: 吴谢(Shieh Ng)
    :url: http://hellowuxie.com
    :copyright: © 2018 Wu Xie <shiehng@gmail.com>
    :license: MIT, see LICENSE for more details.
"""
import requests
import json

login_url = 'http://hubs.hust.edu.cn/hub.jsp'

query_url = 'http://hubs.hust.edu.cn/aam/score/QueryScoreByStudent_queryResults.action'

login_headers = {
    'Cookie': 'username=U201613630; JSESSIONID=0000_kJmtVeXa9ZG2ThuzQOjGdW:166nacc3t',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}

query_data = {
    'xqh': '20161',
    'stuSfid': 'U201613630'
}

query_term = {
    '1': '20161',
    '2': '20162',
    '3': '20171',
    '4': '20172',
    '5': '20181',
    '6': '20182',
    '7': '20191',
    '8': '20192'
}

terms = {
    '20161': '大一上',
    '20162': '大一下',
    '20171': '大二上',
    '20172': '大二下',
    '20181': '大三上',
    '20182': '大三下',
    '20191': '大四上',
    '20192': '大四下'
}

r = requests.Session()
print("正在登录 hub 系统...")
response = r.post(login_url, headers=login_headers)  # 登录 hub 系统
print("登录成功！")

with open('result.txt', 'a') as f:
    f.write("{:<6}{:<10}{:<10}{:<10}{:<10}".format("学期", "科目", "成绩", "学分", "类型"))
    f.write('\n')
    f.write('\n')
    for i in range(1, 6):
        query_data['xqh'] = query_term[str(i)]
        term = terms[query_data['xqh']]

        result = r.post(query_url, data=query_data, headers=login_headers)  # 发送查询成绩请求

        print("正在查询{}学期的成绩".format(term))
        # print(type(result.text))

        data = result.content  # 将查询结果二进制形式存下
        data = json.loads(data)  # 转换为 JSON 对象

        datas = data['score']
        # print(datas)
        for data in datas:
            f.write("{:<6}{:<10}{:<10}{:<10}{:<10}".format(term, data['KCMC'], str(data['XSCJ']), str(data['ZXF']),
                                                               data['CJLX'], chr(12288)))
            f.write('\n')
        f.write('\n')

print("查询完成！")
