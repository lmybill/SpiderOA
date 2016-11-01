#encoding=utf-8

from selenium import webdriver
import time
from bs4 import BeautifulSoup
from util import downloadPDF
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


dr = webdriver.Ie()
dr.maximize_window()
dr.delete_all_cookies()

dr.get("http://oa.bjtelecom.net/")
dr.find_element_by_name('Username').send_keys("A02373")
dr.find_element_by_name('Password').send_keys("a02373")
dr.find_element_by_class_name('login-submit').click()
time.sleep(3)
cookie = dr.get_cookies()
dr.get('http://web.bjtelecom.net/ent_bpms/oa/newsgs/index.jsp?loginedUserID=0')
time.sleep(3)



#集团新闻
def jtNews(soup):
    jtxw = soup.select('#jtxwContent > dl')
    for item in jtxw:
        #print item.a.string
        print item.a['href']
        #print item.dd.string.strip()
        newsUrl = item.a['href']
        if(newsUrl == '*'):
            continue
        dr.get(newsUrl)
        html1 = dr.page_source
        soup1 = BeautifulSoup(html1, 'lxml')
        print soup1.find('h2').contents
        content = soup1.div
        content['class']="wz-content"
        print content
        newsContent = soup1.find_all(id="pageContent")
        break



#省公司新闻
def sgsNews(soup, driver):
    sgsxw = soup.select('#sgsxwContent > dl')
    for item in sgsxw:
        print item.a.string
        #print item.a['href']
        print downloadPDF(dr)
        print item.font.string
        print item.dd.string.strip()


#集团公告
def jtAnnouncement(soup):
    jtgg = soup.select('#jtggContent > ul > li')
    for item in jtgg:
        print item.a.string
        print item.a['href']

#省公司公告
def sgsAnnouncement(soup):
    sgsgg = soup.select('#sgsggContent > ul > li')
    for item in sgsgg:
        print item.a.string
        print item.a['href']

#电信信息
def dxInfo(soup):
    dxxx = soup.select('#dxxxContent > ul > li')
    for item in dxxx:
        print item.a.string
        print item.a['href']

#建言献策
def suggest(soup):
    jyxc = soup.select('#ygjyContent > ul > dl')
    for item in jyxc:
        print item.a.string
        print item.a['href']

#政工信息
def zgInfo(soup):
    zgxx = soup.select('#zgxxContent > dl')
    for item in zgxx:
        print item.a.string
        print item.a['href']
        print item.dd.a.string

#深化改革
def reform(soup):
    shgg = soup.select('ul[class="qh_list"]')[5]
    for item in shgg.select('li'):
        print item.a.string
        print item.a['href']

#法律法规
def law(soup):
    flfg = soup.select('#flfgContent > ul > li')
    for item in flfg:
        print item.a.string
        print item.a['href']


#普法资料
def lawMaterial(soup):
    pfzl = soup.select('#pfzlContent > ul > li')
    for item in pfzl:
        print item.a.string
        print item.a['href']


#权利清单
def rightList(soup):
    qlqd = soup.select('#qlqdContent > ul > li')
    for item in qlqd:
        print item.a.string
        print item.a['href']

#个人待办，待阅，邮件
def personalInfo(drive):
    drive.get('http://web.bjtelecom.net/ent_bpms/oa/newsgs/stay_work.jsp')
    time.sleep(3)
    html = drive.page_source
    soup = BeautifulSoup(html, 'lxml')
    #我的待办
    print "*****************我的待办*********************"
    wddb = soup.select('#wddbContent > dl')
    for item in wddb:
        print item.a['href']
        print item.a.string
        date = item.dd
        print date.string.strip()
        print date.next_sibling.next_sibling.string.strip()

    #我的待阅
    print "*****************我的待阅*********************"
    wddy = soup.select('#wddyContent > dl')
    for item in wddy:
        print item.a['href']
        print item.a.string
        #author = item.dd
        print item.dd.a.string

    #我的邮件
    print "*****************我的邮件*********************"
    wdyj = soup.select('#wdyjContent > dl')
    for item in wdyj:
        print item.a['href']
        print item.a.string
        date = item.dd
        print date.string.strip()
        print date.next_sibling.next_sibling.string.strip()



html = dr.page_source
soup = BeautifulSoup(html, 'lxml')

# print "*****************集团新闻*********************"
# jtNews(soup)
#
print "*****************省公司新闻*********************"
jtNews(soup)
#
# print "*****************集团公告*********************"
# jtAnnouncement(soup)
#
# print "*****************省公司公告*********************"
# sgsAnnouncement(soup)
#
# print "*****************电信信息*********************"
# dxInfo(soup)
#
# print "*****************建言献策*********************"
# suggest(soup)
#
# print "*****************政工信息*********************"
# zgInfo(soup)
#
# print "*****************深化改革*********************"
# reform(soup)
#
# print "*****************法律法规*********************"
# law(soup)
#
# print "*****************普法资料*********************"
# lawMaterial(soup)
#
# print "*****************权利清单*********************"
# rightList(soup)

# print "*****************个人待办待阅*********************"
# personalInfo(dr)

dr.close()