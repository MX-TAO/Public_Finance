import json 
import matplotlib.pyplot as plt 
import re
import msgpack

city = ['shanghai', 'wuhan', 'tianjin']
color = {'shanghai':'r', 'wuhan':'g', 'tianjin':'b'}

data = {}

for c in city:
	data[c] = msgpack.load(open('total_'+c+'.msgpack', 'rb'))

maxy = 0.0
for c in city:
	x = [i[0] for i in data[c]]
	y = [i[1] for i in data[c]]
	maxy = max(maxy, max(y))
	plt.plot(x,y,'k.')
	plt.plot(x,y,color[c]+'-', linewidth=0.75, label=c)

plt.grid(True, 'major', 'both')
plt.xlim((2003.33, 2018.67))
plt.ylim((0, maxy/0.9))
plt.legend()

plt.title('Area of sold lands (hm^2)')
plt.savefig('area.png')
plt.show()

maxy = 0.0
for c in city:
	x = [i[0] for i in data[c]]
	y = [i[2]/100.0 for i in data[c]]
	maxy = max(maxy, max(y))
	plt.plot(x,y,'k.')
	plt.plot(x,y,color[c]+'-', linewidth=0.75, label=c)

plt.grid(True, 'major', 'both')
plt.xlim((2003.33, 2018.67))
plt.ylim((0, maxy/0.9))
plt.legend()

plt.title('Income from sold lands (million RMB yuan)')
plt.savefig('income.png')
plt.show()

maxy = 0.0
for c in city:
	x = [i[0] for i in data[c]]
	y = [i[3] for i in data[c]]
	maxy = max(maxy, max(y))
	plt.plot(x,y,'k.')
	plt.plot(x,y,color[c]+'-', linewidth=0.75, label=c)

plt.grid(True, 'major', 'both')
plt.xlim((2003.33, 2018.67))
plt.ylim((0, maxy/0.9))
plt.legend()

plt.title('Average price of sold lands (RMB yuan / m^2)')
plt.savefig('price.png')
plt.show()

maxy = 0.0
for c in city:
	x = [i[1] for i in data[c]]
	y = [i[2] for i in data[c]]
	maxy = max(maxy, max(y))
	plt.plot(x,y,'k.')
	plt.plot(x,y,color[c]+'-', linewidth=0.75, label=c)

plt.grid(True, 'major', 'both')
plt.legend()
plt.show()