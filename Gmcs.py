## 
#  Get My Course of SUSTech
#  
#  南科大抢课脚本
#  部分代码由BabyXinORZ提供
#  链接: https://github.com/BabyXinORZ/SUSTech-2019Autumn-course_selector
#  使用 python Gmcs.py help 获取帮助
#  
#  @description Eroll once or drop once
#  @author Yvzzi
#  @version 1.0.1
#

from selenium import webdriver
import time
import json
import sys
import os
import requests
from selenium.webdriver.chrome.options import Options

def __getDriver():
    driver = None
    if not DEBUG:
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(options = options)
    else:
        driver = webdriver.Chrome()
    return driver
    

def start(username, pwd, file, times, sleepTime = 0.2):
    bs = __getDriver()
    print("喵! 开始获取凭证!")
    
    url = 'http://jwxt.sustech.edu.cn/jsxsd/framework/xsMain.jsp'
    bs.get(url)
    account = bs.find_element_by_xpath('//*[@id="username"]')
    account.send_keys(username)
    password = bs.find_element_by_xpath('//*[@id="password"]')
    password.send_keys(pwd)
    bs.find_element_by_xpath('//*[@id="fm1"]/section[4]/input[4]').click()
    
    bs.find_element_by_xpath('/html/body/div[5]/a[1]/div').click()

    already = False
    while not already:
        time.sleep(0.005)
        try:
            already = True
            btn2 = bs.find_element_by_xpath('//*[@id="tbKxkc"]/tbody/tr[2]/td[4]/a')
            btn2.click()

        except Exception:
            already = False
            bs.refresh()

    bs.find_element_by_xpath('/html/body/div[3]/div[2]/center/input').click()

    if not os.path.exists("data"):
        os.makedirs("data")
    cookies = bs.get_cookies()
    fp = open("data/credit", "w+")
    fp.write(json.dumps(cookies))
    fp.close()
    
    print("喵! 已经GET凭证!")
    enroll(file, times, sleepTime)
    
    bs.quit()

def enroll(file, times, sleepTime = 0.2):
    fp = open(file, "r+")
    str = fp.read()
    fp.close()
    strs = str.split("\n")
    
    if not os.path.exists("data/credit"):
        print("呜呜, 没找到凭证文件呢")
        exit()
    fp = open("data/credit", "r+")
    creditStr = fp.read()
    fp.close()
    credit = json.loads(creditStr)
    
    if not os.path.exists("data/data"):
        print("呜呜, 没找到数据文件呢")
        exit()
    fp = open("data/data", "r+")
    dataStr = fp.read()
    fp.close()
    data = json.loads(dataStr)
    
    cookies = {
        "JSESSIONID": credit[0]["value"] + "; domain=" + credit[0]["domain"] + "; expires=Session"
    }
    
    header = {
        "Host": "jwxt.sustech.edu.cn",
        "Referer": "https://jwxt.sustech.edu.cn/jsxsd/xsxkkc/comeInBxxk",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }
    
    for t in range(1, int(times) + 1):
        print("喵喵喵x{}! 抢课进行中...".format(t))
        for c in strs:
            if c.strip() == "":
                continue
            rs = requests.get('http://jwxt.sustech.edu.cn/jsxsd/xsxkkc/fawxkOper?jx0404id=' + data[int(c)] + '&xkzy&trjf', cookies = cookies)
            rs.encoding = 'utf-8'
            try:
                ret = json.loads(rs.text)
                status = 'Ok'
                if ret["success"]:
                    status = 'Fail'
                print("{}, {}".format(status, ret["message"]))
            except Exception:
                print("登录失败, 呜呜!")
                print(rs.text)
        time.sleep(float(sleepTime))

def drop(file):
    fp = open(file, "r+")
    str = fp.read()
    fp.close()
    strs = str.split("\n")
    
    if not os.path.exists("data/credit"):
        print("呜呜, 没找到凭证文件呢")
        exit()
    fp = open("data/credit", "r+")
    creditStr = fp.read()
    fp.close()
    credit = json.loads(creditStr)
    
    if not os.path.exists("data/data"):
        print("呜呜, 没找到数据文件呢")
        exit()
    fp = open("data/data", "r+")
    dataStr = fp.read()
    fp.close()
    data = json.loads(dataStr)
    
    cookies = {
        "JSESSIONID": credit[0]["value"] + "; domain=" + credit[0]["domain"] + "; expires=Session"
    }
    
    header = {
        "Host": "jwxt.sustech.edu.cn",
        "Referer": "https://jwxt.sustech.edu.cn/jsxsd/xsxkkc/comeInBxxk",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }
    
    for t in range(1, int(times) + 1):
        print("喵喵喵x{}! 退课进行中...".format(t))
        for c in strs:
            if c.strip() == "":
                continue
            rs = requests.get('http://jwxt.sustech.edu.cn/jsxsd/xsxkjg/xstkOper?jx0404id=' + data[c] + '&xkzy&trjf', cookies = cookies)
            rs.encoding = 'utf-8'
            try:
                ret = json.loads(rs.text)
                status = 'Ok'
                if ret["success"]:
                    status = 'Fail'
                print("{}, {}".format(status, ret["message"]))
            except Exception:
                print("登录失败, 呜呜!")
                print(rs.text)
        time.sleep(float(sleepTime))

def getCredit(username, pwd):
    bs = __getDriver()
    print("喵! 开始获取凭证!")
    
    url = 'http://jwxt.sustech.edu.cn/jsxsd/framework/xsMain.jsp'
    bs.get(url)
    account = bs.find_element_by_xpath('//*[@id="username"]')
    account.send_keys(username)
    password = bs.find_element_by_xpath('//*[@id="password"]')
    password.send_keys(pwd)
    bs.find_element_by_xpath('//*[@id="fm1"]/section[4]/input[4]').click()
    
    bs.find_element_by_xpath('/html/body/div[5]/a[1]/div').click()

    already = False
    while not already:
        time.sleep(0.5)
        try:
            already = True
            select_btn = bs.find_element_by_xpath('//*[@id="tbKxkc"]/tbody/tr[2]/td[4]/a')
            select_btn.click()

        except Exception:
            already = False
            bs.refresh()

    bs.find_element_by_xpath('/html/body/div[3]/div[2]/center/input').click()

    if not os.path.exists("data"):
        os.makedirs("data")
    cookies = bs.get_cookies()
    fp = open("data/credit", "w+")
    fp.write(json.dumps(cookies))
    fp.close()
    
    print("喵! 已经GET凭证!")
    bs.quit()

def getData(username, pwd):
    print("喵! 获取数据中!")
    bs = __getDriver()
    
    # log in
    url = 'https://jwxt.sustech.edu.cn/jsxsd/framework/xsMain.jsp'
    bs.get(url)
    account = bs.find_element_by_xpath('//*[@id="username"]')
    account.send_keys(username)
    password = bs.find_element_by_xpath('//*[@id="password"]')
    password.send_keys(pwd)
    btn_login = bs.find_element_by_xpath('//*[@id="fm1"]/section[4]/input[4]')
    btn_login.click()

    bs.find_element_by_xpath('/html/body/div[5]/a[1]/div').click()

    already = False
    while not already:
        time.sleep(0.05)
        try:
            already = True
            select_btn = bs.find_element_by_xpath('//*[@id="tbKxkc"]/tbody/tr[2]/td[4]/a')
            select_btn.click()

        except Exception:
            already = False
            bs.refresh()

    bs.find_element_by_xpath('/html/body/div[3]/div[2]/center/input').click()

    # course selecting
    all = bs.window_handles
    bs.switch_to.window(all[1])

    data = []
    course = ''
    index = 0
    for menu in range(2, 8):
        bs.find_element_by_xpath('//*[@id="topmenu"]/li[{}]/a'.format(menu)).click()
        
        bs.switch_to.frame("mainFrame")
        
        # wait for loading
        bs.implicitly_wait(5)
        bs.find_elements_by_xpath('//*[@id="dataView_first"]')
        
        pageLength = len(bs.find_elements_by_xpath('//*[@id="dataView_paginate"]/span/a'))
        # print("menu{} pageL{}".format(menu, pageLength))
        for p in range(pageLength):
            bs.find_element_by_xpath('//*[@id="dataView_paginate"]/span/a[{}]'.format(p + 1)).click()
            # print("Enter page{}".format(p + 1))
            bs.implicitly_wait(5)
            # print("items {}".format(len(bs.find_elements_by_xpath('//*[@id="dataView"]/tbody/tr'))))
            
            time.sleep(0.5)
            bs.implicitly_wait(20)
            flag = bs.find_element_by_xpath('//*[@id="dataView"]/tbody/tr[1]/td[1]')
            if flag.text == "对不起，查询不到任何相关数据":
                continue
            
            trs = bs.find_elements_by_xpath('//*[@id="dataView"]/tbody/tr')
            for tr in trs:
                tds = tr.find_elements_by_tag_name("td")
                id = ''
                if menu == 7:
                    id = tds[10].find_element_by_tag_name("div").get_attribute("id")[4:]
                else:
                    id = tds[9].find_element_by_tag_name("div").get_attribute("id")[4:]
                
                tdPos = 6
                totalPos = 7
                if menu == 2:
                    tdPos = 5
                    totalPos = 6
                print('★ 找到课程 {}, {}'.format(
                    tds[0].text.replace("\n", "/").replace(",","/"),
                    tds[1].text.replace("\n", "/").replace(",","/")
                ))
                course = course + ('{}, {}, {}, {}, {}, {}, {}, {}/{}, 菜单第{}项/第{}页\n'.format(
                    index,
                    tds[0].text.replace("\n", "/").replace(",","/"),
                    tds[1].text.replace("\n", "/").replace(",","/"),
                    tds[2].text.replace("\n", "/").replace(",","/"),
                    tds[3].text.replace("\n", "/").replace(",","/"),
                    tds[4].text.replace("\n", "/").replace(",","/"),
                    tds[tdPos].text.replace("\n", "/").replace(",","/"),
                    tds[8].text,
                    tds[totalPos].text,
                    menu,
                    p + 1
                ))
                data.append(id)
                index = index + 1
        
        bs.switch_to.default_content()

    if not os.path.exists("data"):
        os.makedirs("data")
    jsonStr = json.dumps(data)
    fp = open("data/data", "w+")
    fp.write(jsonStr)

    fp.close()
    fp = open("course.csv", "w+")
    fp.write(course)
    fp.close()
    
    print("喵! 搜索完毕惹!")

USAGE = '''Usage:
    抓取课程信息, 课程信息建议提前抓取, 选课时将会用到, 建议在退课期间提前先抓取
    同时抓取信息生成的excel文件可查看所有课程信息(包括人数/总人数等以及所在栏数页数位置), 可供个人选课参考
        {0} data <username> <password>
    
    获得用户凭证
        {0} credit <username> <password>
    
    开始选课, 选课前请先获取到凭证(建议五分钟前), 然后再开始选课, 主要用于测试
        <file> 选课文件, 提供选课内容, 采用类似"0"的课程编号, 编号在生成的course.csv第一列查询
            不同课程间换行符分割
            e.g. 0
                 1
        <times> 尝试次数
        <sleepTime> 休眠时间, 单位为秒, 请酌情设置, 不建议设置太短以免IP被封
        
        {0} enroll <file> <times> <sleepTime>
    
    一键退课, 需要提前获取凭证
        {0} drop <file>
    
    直接获取凭证并选课, 适用于抢课前系统未开放
        {0} start <username> <password> <file> <times> <sleepTime>
        
    查看版本
        {0} version
'''
VERSION = "Get My Course of SUSTech v1.0.1 by Yvzzi"
DEBUG = False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("输入格式不正确")
        print(USAGE.format(sys.argv[0]))
        exit()
    
    if sys.argv[1] == "data" and len(sys.argv) == 4:
        getData(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == "credit" and len(sys.argv) == 4:
        getCredit(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == "enroll" and len(sys.argv) == 5:
        enroll(sys.argv[2], sys.argv[3], sys.argv[4])
    elif sys.argv[1] == "help":
        print(USAGE.format(sys.argv[0]))
    elif sys.argv[1] == "start" and len(sys.argv) == 7:
        start(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
    elif sys.argv[1] == "drop" and len(sys.argv) == 3:
        drop(sys.argv[2])
    elif sys.argv[1] == "version":
        print(VERSION)
    else:
        print("输入格式不正确")
        print(USAGE.format(sys.argv[0]))