from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
import json

browser = webdriver.Chrome('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe')

browser.get('http://ghzyj.sh.gov.cn/tdyxsc/dkxx/')

element = browser.find_element_by_id("zt")
s = Select(element)
s.select_by_value('1')
sb = browser.find_element_by_id("sb")
sb.click()

deal_list = []

sleep(3.0)
"""
count = 0
while True:
	flag = True
	page_list = browser.find_elements_by_tag_name('a')
	for i in page_list:
		page_link = i.get_attribute('href')
		if page_link == None:
			continue
		if 'ghzyj.sh.gov.cn/tdyxsc/dkxx/detail/?id=' in page_link:
			if (page_link in deal_list) == False:
				deal_list.append(page_link)
				flag = False
	count += 1
	print(count, len(deal_list))
	with open('pages.json', 'w', encoding='utf8') as f:
		json.dump(deal_list, f)
	if flag:
		break
	xy = browser.find_element_by_link_text(r'下页')
	xy.click()
	sleep(3.0)
"""
deal_list = json.load(open('pages.json', 'r', encoding='utf8'))
data = []
count = 0
for p in deal_list:
	count += 1
	print(count)
	browser.get(p)
	sleep(0.5)
	d = {}
	e = browser.find_element_by_id('dikmc')
	d['name'] = e.text
	e = browser.find_element_by_id('mianj')
	d['area'] = e.text
	e = browser.find_element_by_id('guihyt')
	d['use']  = e.text
	e = browser.find_element_by_id('rongjl')
	d['ratio'] = e.text
	e = browser.find_element_by_id('churnx')
	d['right'] = e.text
	e = browser.find_element_by_id('zongbj')
	d['price'] = e.text
	e = browser.find_element_by_id('chengjrq')
	d['time'] = e.text
	data.append(d)
	print(d)
	with open('data_shanghai.json', 'w', encoding='utf8') as f:
		json.dump(data, f)

browser.quit()

print(len(deal_list))