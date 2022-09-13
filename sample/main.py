import time
import requests
import json


def send():
    token = 'a19d6e7b73074dc1ab8323491cf4051d'  # 在pushpush网站中可以找到
    title = '抢课成功'  # 改成你要的标题内容
    content = '抢课成功，赶紧去看'  # 改成你要的正文内容
    url = 'http://www.pushplus.plus/send'
    data = {
        "token": token,
        "title": title,
        "content": content
    }
    body = json.dumps(data).encode(encoding='utf-8')
    headers = {'Content-Type': 'application/json'}
    requests.post(url, data=body, headers=headers)


def lesson():
    n = 0
    timestamp = 0.1
    classid = ['76822']
    url = 'http://jwgl.cuit.edu.cn/eams/stdElectCourse!batchOperator.action?profileId=3318'
    cookie = 'semester.id=403; JSESSIONID=568F408E35E336D1EE8F4938118E83BC; ' \
             'UM_distinctid=17b49fe3e8c255-0cfe1359b5ba36-6e577420-240000-17b49fe3e8d10fd; ' \
             'GSESSIONID=568F408E35E336D1EE8F4938118E83BC '
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/95.0.4636.4 Safari/537.36',
        'Referer': 'http://jwgl.cuit.edu.cn/eams/stdElectCourse!defaultPage.action?electionProfile.id=3318',
        'Cookie': cookie
    }
    data0 = {
        'optype': 'true',
        'operator0': classid[0] + ':true:0',
        'lesson0': classid[0],
        'schLessonGroup_' + classid[0]: 'undefined'
    }

    while True:
        time.sleep(timestamp)
        n = n + 1
        print('创践——大学生创新创业实务 课程代码' + str(classid[0]) + str(data0))
        mes = requests.post(url, headers=header, data=data0)
        f = open("res.html", "w")
        res = str(mes.content, 'utf-8')
        if '成功' in res:
            print("创践——大学生创新创业实务 选课成功")
            break
        elif '过快' in res:
            print('过快')
            timestamp = 0.5
        else:
            print('创践——大学生创新创业实务，正在进行第' + str(n) + '次尝试')

        time.sleep(timestamp)
        print('西方艺术史 课程代码' + str(classid[1]) + str(data1))
        mes = requests.post(url, headers=header, data=data1)
        f = open("res.html", "w")
        res = str(mes.content, 'utf-8')
        if '成功' in res:
            print("西方艺术史 选课成功")
            break
        elif '过快' in res:
            print('过快')
            timestamp = 0.5
        else:
            print('西方艺术史 选课失败，正在进行第' + str(n) + '次尝试')

        time.sleep(timestamp)
        print('敦煌的艺术 课程代码' + str(classid[2]) + str(data2))
        mes = requests.post(url, headers=header, data=data2)
        f = open("res.html", "w")
        res = str(mes.content, 'utf-8')
        if '成功' in res:
            print("敦煌的艺术 选课成功")
            break
        elif '过快' in res:
            print('过快')
            timestamp = 0.5
        else:
            print('敦煌的艺术 选课失败，正在进行第' + str(n) + '次尝试')

        time.sleep(timestamp)
        print('大学美育 课程代码' + str(classid[3]) + str(data3))
        mes = requests.post(url, headers=header, data=data3)
        f = open("res.html", "w")
        res = str(mes.content, 'utf-8')
        if '成功' in res:
            print("大学美育 选课成功")
            break
        elif '过快' in res:
            print('过快')
            timestamp = 0.5
        else:
            print('大学美育 选课失败，正在进行第' + str(n) + '次尝试')

        time.sleep(timestamp)
        print('创业修炼 课程代码' + str(classid[4]) + str(data4))
        mes = requests.post(url, headers=header, data=data4)
        f = open("res.html", "w")
        res = str(mes.content, 'utf-8')
        if '成功' in res:
            print("创业修炼 选课成功")
            break
        elif '过快' in res:
            print('过快')
            timestamp = 0.5
        else:
            print('创业修炼 选课失败，正在进行第' + str(n) + '次尝试')

        time.sleep(timestamp)
        print('生态文明 课程代码' + str(classid[5]) + str(data5))
        mes = requests.post(url, headers=header, data=data5)
        f = open("res.html", "w")
        res = str(mes.content, 'utf-8')
        if '成功' in res:
            print("生态文明 选课成功")
            break
        elif '过快' in res:
            print('过快')
            timestamp = 0.5
        else:
            print('生态文明 选课失败，正在进行第' + str(n) + '次尝试')
    f.write(str(mes.content, 'utf-8'))
    time.sleep(1)


def main():
    lesson()
    send()


main()
