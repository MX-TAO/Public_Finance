import msgpack
import json
import re

data = json.load(open('wuhan.json', 'r', encoding='utf8'))

for i in range(len(data)):
	for j in range(len(data[i])):
		for k in range(len(data[i][j])):
			data[i][j][k] = data[i][j][k].replace('\n', '')
			data[i][j][k] = data[i][j][k].replace('\xa0\xa0', ' ')
			data[i][j][k] = data[i][j][k].replace('\xa0', '')
			data[i][j][k] = data[i][j][k].replace('\u3000', ' ')

p_data, r_data = [], []
for i in range(len(data)):
	if len(data[i][0]) <= 12:
		r_data.append(data[i])
		continue

	if data[i][0][4] == r'土地面积（公顷）' and \
		data[i][0][5] == r'土地用途' and \
		data[i][0][6] == r'容积率' and \
		data[i][0][7] == r'建筑面积（㎡）' and \
		data[i][0][8] == r'出让年限' and \
		data[i][0][11][:3] == r'成交价' and \
		data[i][0][12] == r'成交时间' :

		for j in range(1, len(data[i])):
			d = {}
			if len(data[i][j]) < 2 or len(data[i][j][4]) < 1:
				continue
			try:
				float_test = float(data[i][j][11])
			except ValueError:
				continue
			d['area']   = float(data[i][j][4])
			d['usage']  = data[i][j][5]
			d['ratio']  = data[i][j][6]
			d['constr'] = data[i][j][7]
			d['right']  = data[i][j][8]
			d['price']  = float(data[i][j][11])
			d['time']   = data[i][j][12]
			p_data.append(d)
	else:
		r_data.append(data[i])

data = r_data
r_data = []

for i in range(len(data)):
	if len(data[i][0]) <= 12:
		r_data.append(data[i])
		continue

	if data[i][0][4][:4] == r'土地面积' and \
		data[i][0][5] == r'土地用途' and \
		data[i][0][6] == r'容积率' and \
		data[i][0][7][:4] == r'建筑面积' and \
		data[i][0][8] == r'出让年限' and \
		data[i][0][11][:3] == r'成交价' and \
		data[i][0][12] == r'成交时间' :
		
		for j in range(1, len(data[i])):
			d = {}
			if len(data[i][j]) < 2 or len(data[i][j][4]) < 1:
				continue
			try:
				float_test = float(data[i][j][11])
			except ValueError:
				continue
			d['area']   = float(data[i][j][4]) / 10000.0
			d['usage']  = data[i][j][5]
			d['ratio']  = data[i][j][6]
			d['constr'] = data[i][j][7]
			d['right']  = data[i][j][8]
			d['price']  = float(data[i][j][11])
			d['time']   = data[i][j][12]
			p_data.append(d)
	else:
		r_data.append(data[i])

data = r_data
r_data = []

for i in range(len(data)):
	if len(data[i][0]) <= 11:
		r_data.append(data[i])
		continue
	if data[i][0][4][:4] == r'土地面积' and \
		data[i][0][5] == r'土地用途' and \
		data[i][0][6] == r'容积率' and \
		data[i][0][7][:4] == r'建筑面积' and \
		data[i][0][8] == r'出让年限' and \
		data[i][0][10][:3] == r'成交价' and \
		data[i][0][11] == r'成交时间' :

		#print(data[i][0][4], data[i][0][7], data[i][0][10])
		
		for j in range(1, len(data[i])):
			d = {}
			if len(data[i][j]) < 2 or len(data[i][j][4]) < 1:
				continue
			try:
				float_test = float(data[i][j][10])
			except ValueError:
				continue
			d['area']   = float(data[i][j][4])
			d['usage']  = data[i][j][5]
			d['ratio']  = data[i][j][6]
			d['constr'] = data[i][j][7]
			d['right']  = data[i][j][8]
			d['price']  = float(data[i][j][10])
			d['time']   = data[i][j][11]
			p_data.append(d)
	else:
		r_data.append(data[i])

data = r_data
r_data = []

for i in range(len(data)):
	if len(data[i][0]) <= 11:
		r_data.append(data[i])
		continue
	if data[i][0][3][:4] == r'土地面积' and \
		data[i][0][4] == r'土地用途' and \
		data[i][0][5] == r'容积率' and \
		data[i][0][6][:4] == r'建筑面积' and \
		data[i][0][7] == r'出让年限' and \
		data[i][0][10][:3] == r'成交价' and \
		data[i][0][11] == r'成交时间' :

		
		for j in range(1, len(data[i])):
			d = {}
			if len(data[i][j]) < 10 or len(data[i][j][4]) < 1:
				continue
			try:
				float_test = float(data[i][j][10])
			except ValueError:
				continue
			d['area']   = float(data[i][j][3])
			d['usage']  = data[i][j][4]
			d['ratio']  = data[i][j][5]
			d['constr'] = data[i][j][6]
			d['right']  = data[i][j][7]
			d['price']  = float(data[i][j][10])
			d['time']   = data[i][j][11]
			p_data.append(d)
	else:
		r_data.append(data[i])

data = r_data
r_data = []

for i in range(len(data)):
	if len(data[i][0]) <= 9:
		r_data.append(data[i])
		continue
	if data[i][0][4][:4] == r'土地面积' and \
		data[i][0][5] == r'土地用途' and \
		data[i][0][7] == r'容积率' and \
		data[i][0][8].replace(' ', '') == r'出让年限' and \
		data[i][0][9][:3] == r'成交价' and \
		data[i][0][10] == r'成交时间' :

		for j in range(1, len(data[i])):
			d = {}
			if len(data[i][j]) < 10 or len(data[i][j][4]) < 1:
				continue
			try:
				float_test = float(data[i][j][4])
			except ValueError:
				data[i][j][4] = data[i][j][4].split('.')[0:2]
				data[i][j][4] = '.'.join(data[i][j][4])

			d['area']   = float(data[i][j][4])
			d['usage']  = data[i][j][5]
			d['ratio']  = data[i][j][7]
			d['constr'] = ''
			d['right']  = data[i][j][8]
			d['price']  = float(data[i][j][9])
			d['time']   = data[i][j][10]
			p_data.append(d)
	else:
		r_data.append(data[i])

data = r_data
r_data = []

for i in range(len(data)):
	if len(data[i][0]) <= 11:
		r_data.append(data[i])
		continue
	if data[i][0][4][:4] == r'土地面积' and \
		data[i][0][5] == r'土地用途' and \
		data[i][0][8] == r'容积率' and \
		data[i][0][7][:4] == r'建筑面积' and \
		data[i][0][9] == r'出让年限' and \
		data[i][0][11][:3] == r'成交价' and \
		data[i][0][12] == r'成交时间' :
		
		for j in range(1, len(data[i])):
			d = {}
			if len(data[i][j]) < 10 or len(data[i][j][4]) < 1:
				continue
			try:
				float_test = float(data[i][j][10])
			except ValueError:
				continue
			d['area']   = float(data[i][j][4])
			d['usage']  = data[i][j][5]
			d['ratio']  = data[i][j][8]
			d['constr'] = data[i][j][7]
			d['right']  = data[i][j][9]
			d['price']  = float(data[i][j][11])
			d['time']   = data[i][j][12]
			p_data.append(d)
	else:
		r_data.append(data[i])

data = r_data
r_data = []

for i in range(len(data)):
	if len(data[i][0]) <= 9:
		r_data.append(data[i])
		continue
	if data[i][0][4][:4] == r'土地面积' and \
		data[i][0][5] == r'土地用途' and \
		data[i][0][7] == r'容积率' and \
		data[i][0][8][-4:] == r'使用年限' and \
		data[i][0][9][:3] == r'成交价' and \
		data[i][0][10] == r'成交时间' :
		
		for j in range(1, len(data[i])):
			d = {}
			if len(data[i][j]) < 10 or len(data[i][j][4]) < 1:
				continue
			try:
				float_test = float(data[i][j][9])
			except ValueError:
				continue
			d['area']   = float(data[i][j][4].split(r'（')[0])
			d['usage']  = data[i][j][5]
			d['ratio']  = data[i][j][7]
			d['constr'] = ''
			d['right']  = data[i][j][8]
			d['price']  = float(data[i][j][9])
			d['time']   = data[i][j][10]
			p_data.append(d)
	else:
		r_data.append(data[i])

data = r_data
r_data = []

for i in range(len(data)):
	if len(data[i][0]) <= 16:
		r_data.append(data[i])
		continue
	if data[i][0][4][:4] == r'土地面积' and \
		data[i][0][6] == r'用途' and \
		data[i][0][10] == r'容积率' and \
		data[i][0][11][-2:] == r'年限' and \
		data[i][0][12][:3] == r'成交价' and \
		data[i][0][16] == r'成交时间' :
		
		for j in range(1, len(data[i])):
			d = {}
			if len(data[i][j]) < 13 or len(data[i][j][4]) < 1:
				continue
			try:
				float_test = float(data[i][j][12])
			except ValueError:
				continue
			d['area']   = float(data[i][j][4])
			d['usage']  = data[i][j][6]
			d['ratio']  = data[i][j][10]
			d['constr'] = ''
			d['right']  = data[i][j][11]
			d['price']  = float(data[i][j][12])
			d['time']   = data[i][j][16]
			p_data.append(d)
	else:
		r_data.append(data[i])

data = r_data
r_data = []

for i in range(len(data)):
	if len(data[i][0]) <= 11:
		r_data.append(data[i])
		continue
	if data[i][0][4][:4] == r'土地面积' and \
		data[i][0][5] == r'用途' and \
		data[i][0][7] == r'容积率' and \
		data[i][0][8][-2:] == r'年限' and \
		data[i][0][9][:3] == r'成交价' and \
		data[i][0][12] == r'成交时间' :

		for j in range(1, len(data[i])):
			d = {}
			if len(data[i][j]) < 13 or len(data[i][j][4]) < 1:
				continue
			try:
				float_test = float(data[i][j][12])
			except ValueError:
				continue
			d['area']   = float(data[i][j][4])
			d['usage']  = data[i][j][5]
			d['ratio']  = data[i][j][7]
			d['constr'] = ''
			d['right']  = data[i][j][8]
			d['price']  = float(data[i][j][9])
			d['time']   = data[i][j][12]
			p_data.append(d)
	else:
		r_data.append(data[i])

data = r_data
r_data = []

for i in range(len(data)):
	if len(data[i][0]) <= 11:
		r_data.append(data[i])
		continue
	if data[i][0][4][:4] == r'土地面积' and \
		data[i][0][6] == r'用途' and \
		data[i][0][10] == r'容积率' and \
		data[i][0][11][-2:] == r'年限' and \
		data[i][0][12][:2] == r'地价' and \
		data[i][0][16] == r'成交时间' :
		
		for j in range(1, len(data[i])):
			d = {}
			if len(data[i][j]) < 13 or len(data[i][j][4]) < 1:
				continue
			try:
				float_test = float(data[i][j][12])
			except ValueError:
				continue
			d['area']   = float(data[i][j][4])
			d['usage']  = data[i][j][6]
			d['ratio']  = data[i][j][10]
			d['constr'] = ''
			d['right']  = data[i][j][11]
			d['price']  = float(data[i][j][12])
			d['time']   = data[i][j][16]
			p_data.append(d)
	else:
		r_data.append(data[i])

data = r_data
r_data = []

wl = [r'土地面积', r'用途', r'容积率', r'年限', r'成交价', r'成交时间']
wr = [4, -2, 3, -2, 3, 4]
for i in range(len(data)):
	idx = []
	for w, r in zip(wl, wr):
		for j in range(len(data[i][0])):
			if r<0:
				strr = data[i][0][j][r:]
			else:
				strr = data[i][0][j][:r]
			if strr == w:
				idx.append(j)
	if len(idx) == 6:
		for j in range(1, len(data[i])):
			d = {}
			if len(data[i][j]) < 6:
				continue
			try:
				float_test = float(data[i][j][idx[0]])
			except ValueError:
				continue
			d['area']   = float(data[i][j][idx[0]])
			d['usage']  = data[i][j][idx[1]]
			d['ratio']  = data[i][j][idx[2]]
			d['constr'] = ''
			d['right']  = data[i][j][idx[3]]
			d['price']  = float(data[i][j][idx[4]])
			d['time']   = data[i][j][idx[5]]
			p_data.append(d)
	else:
		r_data.append(data[i])

data = r_data
r_data = []

for i in data:
	if len(i[0]) ==0:
		continue
	if i[0][0][-8:] == r'公开出让活动结果' and i[1][0][:5] == r'（活动日期':
		ti = i[1][0][6:].split(r'日')[0]
		for j in range(4, len(i)):
			try:
				float_test = float(i[j][9])
				i[j][2] = i[j][2].replace('(', r'（')
				float_test = float(i[j][2])
			except ValueError:
				continue
			print([i[j][2], i[j][4], i[j][5], i[j][6], i[j][9]])
			d = {}
			d['area']   = float(i[j][2].split(r'（')[0]) / 10000.0
			d['usage']  = i[j][4]
			d['ratio']  = i[j][5]
			d['constr'] = ''
			d['right']  = i[j][6]
			d['price']  = i[j][9]
			d['time']   = ti
			p_data.append(d)
	else:
		r_data.append(i)

data = r_data
r_data = []

wl = [r'土地面积', r'用途', r'容积率', r'年限', r'成交价', r'成交时间']
wr = [4, -2, 3, -2, 3, 4]
for i in range(len(data)):
	if data[i][0][0][-3:] == r'信息表':
		idx = []
		for w, r in zip(wl, wr):
			for j in range(len(data[i][1])):
				if r<0:
					strr = data[i][1][j][r:]
				else:
					strr = data[i][1][j][:r]
				if strr == w:
					idx.append(j)
		if len(idx) == 6:
			for j in range(2, len(data[i])):
				d = {}
				if len(data[i][j]) < 6:
					continue
				try:
					float_test = float(data[i][j][idx[0]])
					float_test = float(data[i][j][idx[4]])
				except ValueError:
					continue
				d['area']   = float(data[i][j][idx[0]])
				d['usage']  = data[i][j][idx[1]]
				d['ratio']  = data[i][j][idx[2]]
				d['constr'] = ''
				d['right']  = data[i][j][idx[3]]
				d['price']  = float(data[i][j][idx[4]])
				d['time']   = data[i][j][idx[5]]
				p_data.append(d)
		else:
			r_data.append(data[i])
	else:
		r_data.append(data[i])

data = r_data
r_data = []

for i in range(len(data)):
	if len(data[i][0]) <= 11:
		r_data.append(data[i])
		continue
	if data[i][0][5][:5] == r'净用地面积' and \
		data[i][0][4] == r'规划用途' and \
		data[i][0][6] == r'容积率' and \
		data[i][0][9][:4] == r'出让价款':
		
		for j in range(1, len(data[i])):
			d = {}
			if len(data[i][j]) < 10 or len(data[i][j][4]) < 1:
				continue
			try:
				float_test = float(data[i][j][9])
			except ValueError:
				continue
			d['area']   = float(data[i][j][5]) / 10000.0
			d['usage']  = data[i][j][4]
			d['ratio']  = data[i][j][6]
			d['constr'] = ''
			d['right']  = ''
			d['price']  = float(data[i][j][9])
			d['time']   = '2011-01-01'
			p_data.append(d)
	else:
		r_data.append(data[i])

data = r_data
r_data = []

for i in data:
	if len(i[1]) > 1 and i[1][0][:4] == r'土地面积':
		for j in range(0, len(i), 4):
			d = {}
			d['usage']  = i[j][5]
			d['area']   = float(i[j+1][1])
			d['ratio']  = ''
			d['constr'] = ''
			d['right']  = i[j+1][3]
			d['price']  = float(i[j+1][5])
			d['time']   = i[j][1].split(r'（')[1].split(r'）')[0] + '-01-01'
			p_data.append(d)
	else:
		r_data.append(i)

data = r_data
r_data = []


wl = [r'出让面积', r'容积率', r'土地用途', r'成交价']
wr = [4, 3, 4, 3]
for i in range(len(data)):
	da= re.compile('\d+\.\d+\.\d+')
	if len(da.findall(data[i][0][0]))>0:
		ti = da.findall(data[i][0][0])[0]
		idx = []
		for w, r in zip(wl, wr):
			for j in range(len(data[i][1])):
				if r<0:
					strr = data[i][1][j][r:].replace(' ', '')
				else:
					strr = data[i][1][j][:r].replace(' ', '')
				if strr == w:
					idx.append(j)
		if len(idx) == 4:
			for j in range(2, len(data[i])):
				d = {}
				if len(data[i][j]) < 4:
					continue
				try:
					float_test = float(data[i][j][idx[0]])
					float_test = float(data[i][j][idx[3]])
				except ValueError:
					continue
				d['area']   = float(data[i][j][idx[0]]) / 10000.0
				d['usage']  = ''
				d['ratio']  = data[i][j][idx[1]]
				d['constr'] = ''
				d['right']  = data[i][j][idx[2]]
				d['price']  = float(data[i][j][idx[3]])
				d['time']   = ti
				p_data.append(d)
		else:
			r_data.append(data[i])
	else:
		r_data.append(data[i])

data = r_data
r_data = []


wl = [r'编号', r'面积', r'用途', r'成交价']
for i in data:
	idx = []
	for w in wl:
		for j in range(len(i[0])):
			if w in i[0][j].replace(' ', ''):
				idx.append(j)
				break
	if len(idx) == 4:
		da= re.compile('\d{4}')
		for j in range(1, len(i)):
			if len(i[j]) > len(i[0]):
				i[j].pop(2)
			if len(i[j]) < 3:
				continue
			try:
				float_test = float(i[j][idx[1]])
				float_test = float(i[j][idx[3]])
			except ValueError:
				continue
			if len(da.findall(i[j][idx[0]])) > 0:
				ti = da.findall(i[j][idx[0]])[0]
				d = {}
				d['usage']  = ''
				d['area']   = float(i[j][idx[1]])
				if d['area'] > 150:
					d['area'] /= 10000.0
				d['ratio']  = ''
				d['constr'] = ''
				d['right']  = i[j][idx[2]]
				d['price']  = float(i[j][idx[3]])
				d['time']   = ti + '-01-01'
				p_data.append(d)
	else:
		r_data.append(i)

data = r_data
r_data = []

wl = [r'编号', r'面积', r'成交']
for i in data:
	idx = []
	for w in wl:
		for j in range(len(i[0])):
			if w in i[0][j].replace(' ', ''):
				idx.append(j)
				break
	if len(idx) == 3:
		da= re.compile('\d{4}')
		for j in range(1, len(i)):
			if len(i[j]) > len(i[0]):
				i[j].pop(2)
			if len(i[j]) < 3:
				continue
			try:
				float_test = float(i[j][idx[1]])
				float_test = float(i[j][idx[2]])
			except ValueError:
				continue
			except IndexError:
				continue
			if len(da.findall(i[j][idx[0]])) > 0:
				ti = da.findall(i[j][idx[0]])[0]
				d = {}
				d['usage']  = ''
				d['area']   = float(i[j][idx[1]])
				if d['area'] > 150:
					d['area'] /= 10000.0
				d['ratio']  = ''
				d['constr'] = ''
				d['right']  = ''
				d['price']  = float(i[j][idx[2]])
				d['time']   = ti + '-01-01'
				p_data.append(d)
	else:
		r_data.append(i)

data = r_data
r_data = []

wl = [r'编号', r'面积', r'成交']
for i in data:
	_i = i
	i = i[1:]
	idx = []
	for w in wl:
		for j in range(len(i[0])):
			if w in i[0][j].replace(' ', ''):
				idx.append(j)
				break
	if len(idx) == 3:
		da= re.compile('\d{4}')
		for j in range(1, len(i)):
			if len(i[j]) > len(i[0]):
				i[j].pop(2)
			if len(i[j]) < 3:
				continue
			try:
				float_test = float(i[j][idx[1]])
				float_test = float(i[j][idx[2]])
			except ValueError:
				continue
			except IndexError:
				continue
			if len(da.findall(i[j][idx[0]])) > 0:
				ti = da.findall(i[j][idx[0]])[0]
				d = {}
				d['usage']  = ''
				d['area']   = float(i[j][idx[1]])
				if d['area'] > 150:
					d['area'] /= 10000.0
				d['ratio']  = ''
				d['constr'] = ''
				d['right']  = ''
				d['price']  = float(i[j][idx[2]])
				d['time']   = ti + '-01-01'
				p_data.append(d)
	else:
		r_data.append(_i)

data = r_data
r_data = []


wl = [r'编号', r'面积', r'成交']
for i in data:
	if len(i)<=2:
		continue
	_i = i
	i = i[2:]
	idx = []
	for w in wl:
		for j in range(len(i[0])):
			if w in i[0][j].replace(' ', ''):
				idx.append(j)
				break
	if len(idx) == 3:
		da= re.compile('\d{4}')
		for j in range(1, len(i)):
			if len(i[j]) > len(i[0]):
				i[j].pop(2)
			if len(i[j]) < 3:
				continue
			try:
				float_test = float(i[j][idx[1]])
				float_test = float(i[j][idx[2]])
			except ValueError:
				continue
			except IndexError:
				continue
			if len(da.findall(i[j][idx[0]])) > 0:
				ti = da.findall(i[j][idx[0]])[0]
				d = {}
				d['usage']  = ''
				d['area']   = float(i[j][idx[1]])
				if d['area'] > 150:
					d['area'] /= 10000.0
				d['ratio']  = ''
				d['constr'] = ''
				d['right']  = ''
				d['price']  = float(i[j][idx[2]])
				d['time']   = ti + '-01-01'
				p_data.append(d)
	else:
		r_data.append(_i)

data = r_data
r_data = []
print(len(data))

for i in data:
	print(i[2])

json.dump(p_data, open('pure_wuhan.json', 'w', encoding='utf8'))