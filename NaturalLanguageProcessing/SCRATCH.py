d = {'banana': 3, 'orange': 5, 'apple': 5}
temp = sorted(d.items(), key=lambda x: (-x[1], x[0]))

temp2 = [i[0] for i in temp]

print(''.join(temp2))