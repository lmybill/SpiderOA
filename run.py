#encoding=utf-8
import urllib
import urllib2


#values = {"%%ModDate": "2FB15DFA00000000", "Username": "A02373", "Password": "a02373", "x": 144, "y": 28, "RedirectTo": "/bjteloa/HomePage.nsf/Index?openframeset&login"}
values = {}
values['%%ModDate'] = "2FB15DFA00000000"
values['Username'] = "A02373"
values['Password'] = "a02373"
values['x'] = "343"
values['y'] = "41"
values['RedirectTo'] = "/bjteloa/HomePage.nsf/Index?openframeset&login"
data = urllib.urlencode(values)
print data
url = 'http://oa.bjtelecom.net/names.nsf?Login'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0'
referer = 'http://oa.bjtelecom.net/'
contentType = 'application/x-www-form-urlencoded'
headers = {'User-Agent': user_agent, 'Referer': referer, 'Content-Type': contentType}
request = urllib2.Request(url, data, headers)
try:
    response = urllib2.urlopen(request)
    print response.read()
except urllib2.HTTPError, e:
    print e.code
    print e.reason
