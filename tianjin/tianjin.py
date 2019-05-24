from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
import json
import random
import re

from Functions import *

user_agent = [
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12;) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
]

#browser = webdriver.Chrome('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe')

"""
browser.get('http://gh.tj.gov.cn/newslist.aspx?id=CK530303')

element = browser.find_element_by_id('zt')
s = Select(element)
s.select_by_value('1')
sb = browser.find_element_by_id('sb')
sb.click()


deal_list = []

sleep(1.0)

count = 0
while True:
	flag = True
	page_list = browser.find_elements_by_tag_name('a')
	for i in page_list:
		page_link = i.get_attribute('href')
		if page_link == None:
			continue
		if 'gh.tj.gov.cn/news.aspx?id=' in page_link:
			if (page_link in deal_list) == False:
				deal_list.append(page_link)
				flag = False
	count += 1
	print(count, len(deal_list))
	with open('pages.json', 'w', encoding='utf8') as f:
		json.dump(deal_list, f)
	if flag:
		break
	xy = browser.find_element_by_link_text(r'下一页')
	xy.click()
	sleep(1.0)

deal_list = json.load(open('pages.json', 'r', encoding='utf8'))


pages_detail = []
count = 0
for p in deal_list:
	count += 1
	print(count)
	html_text = getHTMLText(p, _headers=user_agent[random.randint(0, len(user_agent)-1)])
	pages_detail.append(html_text.text)
	if count % 25 == 0:
		with open('pages_detail.json', 'w', encoding='utf8') as f:
			json.dump(pages_detail, f)
	sleep(0.05)

with open('pages_detail.json', 'w', encoding='utf8') as f:
	json.dump(pages_detail, f)

pages_detail = json.load(open('pages_detail.json', 'r', encoding='utf8'))
pages_part = []
head = re.compile('<font color ="#8c8a8c">\d{4}/\d\d?/\d\d?')
for i in range(len(pages_detail)):
	headstr = head.findall(pages_detail[i])[0]
	sloc = pages_detail[i].find(headstr)
	eloc = pages_detail[i].find(r'附件')
	part = pages_detail[i][sloc+len(headstr):eloc]
	part = part[part.find('</font>'):]
	pages_part.append(part)

with open('pages_part.json', 'w', encoding='utf8') as f:
	json.dump(pages_part, f)

pages_part = json.load(open('pages_part.json', 'r', encoding='utf8'))
pages_str = []

ntag = re.compile('>(.*?)<')
for i in range(len(pages_part)):
	p = pages_part[i]
	p = p.replace('<span>', '')
	p = p.replace('</span>', '')
	p = p.replace('<br>', ' ')
	p = p.replace('<p>', ' ')
	p = p.replace('\n', ' ')
	p = p.replace('\r', ' ')
	#print(i)
	#print(p)
	#print('------')
	p = ' '.join(ntag.findall(p))
	#print(p)
	#print('------')
	while '  ' in p:
		p = p.replace('  ', ' ')

	if len(p) < 30:
		continue
	
	#print(p)
	pages_str.append(p)

with open('pages_str.json', 'w', encoding='utf8') as f:
	json.dump(pages_str, f)

"""


pages_str = json.load(open('pages_str.json', 'r', encoding='utf8'))
num = re.compile(r'\d+\.?\d*.')
num2 = re.compile(r'\d+\.?\d*')
date = re.compile(r'\d{4}.\d\d?.\d\d?')
md = re.compile(r'\d\d?.\d\d?')
data = []
for i in range(len(pages_str)):
	if (r'面积' in pages_str[i]) == False:
		continue
	if (r'价格' in pages_str[i] or r'成交价' in pages_str[i]) == False:
		continue
	d = {}

	area = num.findall(pages_str[i][pages_str[i].find(r'面积'):])[0]
	try:
		area = float(area)
	except ValueError:
		area = float(area[:-1])

	if area < 10:
		continue

	if r'价格' in pages_str[i]:
		price = num.findall(pages_str[i][pages_str[i].find(r'价格'):])[0]
		tmp = pages_str[i][pages_str[i].find(r'价格'):pages_str[i].find(r'价格')+8]
	else:
		price = num.findall(pages_str[i][pages_str[i].find(r'成交价'):])[0]
		tmp = pages_str[i][pages_str[i].find(r'成交价'):pages_str[i].find(r'成交价')+8]
	if price[0] == '0':
		continue
	if r'万' in tmp:
		price = price + r'万'

	if price[-1] == r'万':
		mul = 10000.0
	else:
		mul = 1.0
	price = mul * float(num2.findall(price)[0])
	if price/area < 20 and price < 1e6:
		price *= 10000.0

	ti = date.findall(pages_str[i][pages_str[i].find(r'日期'):])
	if len(ti) < 1:
		ti = md.findall(pages_str[i])[0]
		year = re.compile(r'挂.*?\d{4}')
		ti = year.findall(pages_str[i])[0][-4:] + ' ' + ti
	else:
		ti = ti[0]

	d['time'] = ti
	d['price'] = price
	d['area'] = area

	data.append(d)

with open('data_tianjin.json', 'w', encoding='utf8') as f:
	json.dump(data, f)

#browser.quit()

#print(len(deal_list))