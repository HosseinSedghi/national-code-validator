import pprint as pn

op = open('city codes.txt', encoding='utf-8', mode='r').readlines()

x = {}
y = ''
is_y = False

for line in op:

	i = line.strip().split('\t')
	if i[0] == '***':
		y = i[1]
		is_y = True

	if not is_y:
		if '-' in i[0]:
			m = i[0].split('-')
			for a in m:
				x[a] = i[1], y
		else:
			x[i[0]] = i[1], y
	else:
		is_y = False

pn.pprint(x)