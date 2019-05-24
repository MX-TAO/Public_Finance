import json 
import matplotlib.pyplot as plt 
import re
import msgpack

a = json.load(open('data_shanghai3.json', 'r', encoding='utf8'))
k = [0.0] * 2024
k2 = [0.0] * 2024
for i in range(len(a)):
	year = re.compile('\d{4}')
	y = year.findall(a[i]['time'])
	k[int(y[0])] += (float(a[i]['area']) / 10000.0)
	k2[int(y[0])] += float(a[i]['price'])

plt.grid(True, 'major', 'both')

x = list(range(2004, 2019))
y1 = k[2004:2019]

plt.ylim((0, max(y1)/0.9))
plt.xlim((2003.33, 2018.67))
for i in range(len(x)):
	plt.plot(x[i], y1[i], 'r.')
plt.plot(x, y1, 'k-', linewidth=0.75)
plt.title('Area of sold lands (hm^2) -- Shanghai')
plt.savefig('shanghai1.png')
plt.show()

plt.grid(True, 'major', 'both')

y2 = k2[2004:2019]
y2 = [i/100 for i in y2]
plt.ylim((0, max(y2)/0.9))
plt.xlim((2003.33, 2018.67))
for i in range(len(x)):
	plt.plot(x[i], y2[i], 'b.')
plt.plot(x, y2, 'k-', linewidth=0.75)
plt.title('Income from sold lands (million RMB yuan) -- Shanghai')
plt.savefig('shanghai2.png')
plt.show()

plt.grid(True, 'major', 'both')

y3 = [y2[i]/y1[i]*100 for i in range(len(y1))]
plt.ylim((0, max(y3)/0.9))
plt.xlim((2003.33, 2018.67))
for i in range(len(x)):
	plt.plot(x[i], y3[i], 'g.')
plt.plot(x, y3, 'k-', linewidth=0.75)
plt.title('Average price of sold lands (RMB yuan / m^2) -- Shanghai')
plt.savefig('shanghai3.png')
plt.show()

print(y1)
print(y2)

b = []
for i in range(len(y1)):
	print('%d,%.5f,%.6f,%.2f'%(i+2004, y1[i], y2[i]*100.0, y3[i]))
	b.append([i+2004, y1[i], y2[i]*100.0, y3[i]])

msgpack.dump(b, open('../total/total_shanghai.msgpack', 'wb'))