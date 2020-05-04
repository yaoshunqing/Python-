# @Time : 2020/4/27 20:31
# @Author : Yao
# @File : alien.py
# @Software: PyCharm

alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

#添加键值对

alien_0['x_position'] = 0
alien_0['y_position'] = 0

print(alien_0)


del alien_0['points']
print(alien_0)

#遍历所有的键值对
#for key,value in alien_0.items():
for k,v in alien_0.items():
	print('\nKey: ' + k)
	print('Value: ' + str(v))

print('\n')
#遍历所有的键

for name in alien_0.keys():
	print(name)

#遍历所有的值
for value in alien_0.values():
	print(value)

print('\n')
#字典列表
aliens =[]

#创建30个绿色的外星人
for alien_number in range(30):
	new_alien = {'color':'green','points':5,'speed':'slow'}
	aliens.append(new_alien)

for alien in aliens[0:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10


#显示前五个外星人
for alien in aliens[:5]:
	print(alien)
print("...")

print("Total number of aliens: " + str(len(aliens)))




